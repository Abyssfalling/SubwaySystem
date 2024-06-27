# handlers.py
import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox, simpledialog
import re  # 导入正则表达式库
import data_management
import utils


def add_line_window():
    """Open a new window to input details for a new subway line, ensuring all fields are required."""
    window = Toplevel()
    window.title("添加新线路")

    Label(window, text="线路ID:").pack()
    line_id_entry = Entry(window)
    line_id_entry.pack()

    Label(window, text="线路名称:").pack()
    line_name_entry = Entry(window)
    line_name_entry.pack()

    Label(window, text="站点（使用逗号分隔）:").pack()
    stations_entry = Entry(window)
    stations_entry.pack()

    submit_btn = Button(window, text="提交", command=lambda: submit_new_line(
        line_id_entry.get(), line_name_entry.get(), stations_entry.get(), window))
    submit_btn.pack()


def submit_new_line(line_id, line_name, stations, window):
    """Handle the submission of a new line, ensuring no fields are empty."""
    if not line_id.strip() or not line_name.strip() or not stations.strip():
        # 如果任何一个输入为空，显示错误信息
        messagebox.showerror("输入错误", "所有字段均为必填项，请确保填写所有信息。")
        return

    stations_list = re.split(r'[ ,，]+', stations.strip())
    if not stations_list:
        messagebox.showerror("输入错误", "至少需要一个站点。")
        return

    success = data_management.add_line(line_id, line_name, stations_list)
    if success:
        window.destroy()
        data_management.save_data()  # 添加成功后保存数据
        messagebox.showinfo("成功", "新线路添加成功，并已保存数据。")
    else:
        # 如果添加失败（例如ID重复），保留窗口开启，允许用户更正
        pass


def add_neighboring_station(station, data, canvas, line_id):
    def submit():
        new_station_name = entry.get()
        position = var.get()
        # 确保输入不为空
        if not new_station_name.strip():
            tk.messagebox.showerror("错误", "站点名称不能为空")
            return
        # 找到当前站点在data中的位置，并根据选择插入新站点
        for line in data['lines']:
            for idx, st in enumerate(line['stations']):
                if st['stationName'] == station['stationName']:
                    if position == 'prev':
                        line['stations'].insert(idx, {"stationID": str(idx), "stationName": new_station_name,
                                                      "lineID": line_id})
                    else:
                        line['stations'].insert(idx + 1, {"stationID": str(idx + 1), "stationName": new_station_name,
                                                          "lineID": line_id})
                    break
        # 更新站点ID
        for line in data['lines']:
            for idx, st in enumerate(line['stations']):
                st['stationID'] = str(idx)
        # 保存数据
        data_management.save_data()
        window.destroy()

        # 更新数据后重新绘制线路
        line = data_management.get_line(line_id)
        if line:
            utils.draw_line(canvas, line, data)

    window = Toplevel()
    window.title("增加邻近站点")

    var = tk.StringVar(value="next")
    tk.Radiobutton(window, text="增加上一站", variable=var, value="prev").pack()
    tk.Radiobutton(window, text="增加下一站", variable=var, value="next").pack()

    Label(window, text="站点名称:").pack()
    entry = Entry(window)
    entry.pack()

    Button(window, text="提交", command=submit).pack()


def delete_station(station, data, canvas, line_id):
    response = tk.messagebox.askyesno("确认删除", f"您确定要删除站点{station['stationName']}吗？")
    if response:
        # 从data中找到并删除站点
        for line in data['lines']:
            # 过滤掉要删除的站点
            new_stations = [st for st in line['stations'] if st['stationName'] != station['stationName']]
            # 如果新站点列表为空，则删除整条线路
            if not new_stations:
                data['lines'].remove(line)
                tk.messagebox.showinfo("线路删除", f"已删除整条线路：{line['lineName']}，因为没有其他站点。")
            else:
                line['stations'] = new_stations
                # 更新站点ID
                for idx, st in enumerate(line['stations']):
                    st['stationID'] = str(idx + 1)

        # 删除与该站点相关的所有换乘关系
        data['transfers'] = [t for t in data['transfers'] if
                             t['fromStation'] != station['stationName'] and t['toStation'] != station['stationName']]

        # 保存数据
        data_management.save_data()
        messagebox.showinfo("删除成功", "站点已删除，并更新了数据。")

        # 更新数据后重新绘制线路
        line = data_management.get_line(line_id)
        if line:
            utils.draw_line(canvas, line, data)
        else:
            canvas.delete("all")  # 如果线路被删除，则清空 Canvas


def view_transfers(station, data, canvas):
    window = tk.Toplevel()
    window.title(f"换乘情况 - {station['stationName']}")

    window.geometry('300x200')

    # 筛选以当前站点为起点的换乘关系，并按照目的线路ID和目的站点名称排序
    transfers = [t for t in data['transfers'] if
                 t['fromStation'] == station['stationName'] and t['fromLine'] == station['lineID']]
    transfers.sort(key=lambda x: (x['toLine'], x['toStation']))  # 根据目的线路ID和站点名称排序

    listbox = tk.Listbox(window)
    for t in transfers:
        listbox.insert(tk.END, f"从 {t['fromLine']} 线 {t['fromStation']} 换乘到 {t['toLine']} 线 {t['toStation']}")
    listbox.pack(fill=tk.BOTH, expand=True)

    # 删除和添加换乘站的按钮
    delete_button = tk.Button(window, text="删除该换乘站",
                              command=lambda: delete_transfer(transfers, listbox, data, canvas, station['lineID']))
    delete_button.pack(side=tk.LEFT)
    add_button = tk.Button(window, text="添加换乘站", command=lambda: add_transfer(station, data, canvas, listbox))
    add_button.pack(side=tk.RIGHT)

    # 这里还需要确保更新画布后显示正确的线路
    listbox.bind('<<ListboxSelect>>',
                 lambda event: utils.update_canvas_on_select(event, canvas, data, station['lineID']))


def add_transfer(station, data, canvas, listbox):
    line_id = station['lineID']  # 直接从站点数据中获取 lineID
    transfer_window = tk.Toplevel()
    transfer_window.title("添加换乘站")

    main_frame = tk.Frame(transfer_window)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 下拉菜单选择线路，排除当前站点所在的线路
    line_var = tk.StringVar(transfer_window)
    line_options = [line['lineName'] for line in data['lines'] if line['lineID'] != line_id]
    if line_options:  # 确保至少有一个选项可用
        line_menu = tk.OptionMenu(main_frame, line_var, *line_options)
    else:
        line_menu = tk.OptionMenu(main_frame, line_var, "无可用线路")
    line_menu.pack()

    # 下拉菜单选择站点，初始化为空
    station_var = tk.StringVar(transfer_window)
    station_menu = tk.OptionMenu(main_frame, station_var, "选择站点")
    station_menu.pack()

    # 更新站点菜单的函数
    def update_station_menu(*args):
        selected_line = next((line for line in data['lines'] if line['lineName'] == line_var.get()), None)
        if selected_line:
            station_options = [st['stationName'] for st in selected_line['stations']]
            station_menu['menu'].delete(0, 'end')
            for station_name in station_options:
                station_menu['menu'].add_command(label=station_name, command=tk._setit(station_var, station_name))
        else:
            station_menu['menu'].delete(0, 'end')
            station_menu['menu'].add_command(label="无站点", command=tk._setit(station_var, "无站点"))

    line_var.trace('w', update_station_menu)  # 当选中的线路变化时更新站点选项

    def confirm_transfer():
        to_line = next((line for line in data['lines'] if line['lineName'] == line_var.get()), None)
        if to_line and not any(t['fromStation'] == station['stationName'] and t['toStation'] == station_var.get() for t in data['transfers']):
            new_transfer = {
                "fromLine": line_id,
                "fromStation": station['stationName'],
                "toLine": to_line['lineID'],
                "toStation": station_var.get()
            }
            data['transfers'].append(new_transfer)
            data_management.save_data()
            listbox.insert(tk.END, f"{new_transfer['fromLine']} 线 {new_transfer['fromStation']} 到 {new_transfer['toLine']} 线 {new_transfer['toStation']}")
            transfer_window.destroy()
            # 刷新画布以显示更新
            line = data_management.get_line(line_id)
            if line:
                utils.draw_line(canvas, line, data)

    confirm_button = tk.Button(transfer_window, text="确定", command=confirm_transfer)
    confirm_button.pack()



def delete_transfer(transfers, listbox, data, canvas, line_id):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        transfer = transfers[index]
        confirm = tk.messagebox.askyesno("确认删除",
                                         f"确认删除从 {transfer['fromLine']} 线 {transfer['fromStation']} 换乘到 {transfer['toLine']} 线 {transfer['toStation']} 的换乘关系及其反向关系吗？")
        if confirm:
            # 删除当前换乘及其反向换乘
            data['transfers'] = [t for t in data['transfers'] if not (
                    (t['fromStation'] == transfer['fromStation'] and t['toStation'] == transfer['toStation']) or
                    (t['fromStation'] == transfer['toStation'] and t['toStation'] == transfer['fromStation'])
            )]
            data_management.save_data()
            listbox.delete(index)  # 删除列表中的项
            tk.messagebox.showinfo("删除成功", "换乘关系已删除")

            # 更新数据后重新绘制线路
            line = data_management.get_line(line_id)
            if line:
                utils.draw_line(canvas, line, data)
            else:
                canvas.delete("all")  # 如果线路被删除，则清空 Canvas


def query_line_info(canvas):
    """Prompt user for a line ID and display the line on the canvas if found."""
    line_id = simpledialog.askstring("Query Line", "Enter the line ID:")
    line = data_management.get_line(line_id)
    if line:
        utils.draw_line(canvas, line, data_management.data)  # Pass the entire data if needed
    else:
        messagebox.showerror("Error", "Line not found.")


def exit_application():
    """Exit the application."""
    import sys
    sys.exit(0)
