# 小组任务：上海地铁路线查询系统

[TOC]

# 1 问题描述

## 1.1 系统概述

本系统旨在提供一个用户友好的地铁路线查询服务，允许用户输入和修改地铁线路信息，并查询从起点到终点的路线。

## 1.2 基本功能

### 1.2.1 线路信息输入

​	**用户能够输入地铁线路编号和站点信息。**

### 1.2.2 换乘站信息输入

​	**用户能够输入换乘站信息。**

### 1.2.3 线路信息修改

​	**扩充线路长度：**例如，将9号线的站点数量从35增加到40。

​	**缩短线路长度：**例如，将9号线的站点数量从35减少到30。

​	**删除换乘站：**允许用户删除指定线路间的换乘关系，例如删除9号线和3号线的yishanlu站的换乘。

​	**封闭线路区间：**例如，封闭9号线的第16站至第18站，使得这三站无法出入或进行换乘。

​	**恢复线路区间：**例如，恢复9号线的第16站

### 1.2.4 线路查询功能

​	**输入线路号查询：**例如，输入9，可以输出9号线的站点以及换乘信息。

### 1.2.5 路线查询功能

以上线路信息中，每两站之间距离均为1，所有换乘距离均为0。用户可以查询从某一站点到另一站点的最短路线。系统将输出以下结果之一：

​	**无需换乘则输出路线和起止站点。**例如，输入“songjiangdaxuecheng shijidadao”，则输出“乘坐9号线 songjiangdaxuecheng上车， shijidadao下车”

​	**换乘路线所有必要的换乘站点和线路。**例如，输入“songjiangdaxuecheng zhongshangongyuan”，则输出“9号线 songjiangdaxuecheng上， yishanlu下\n3号线yishanlu上，zhongshangongyuan下”以及“9号线 songjiangdaxuecheng上， yishanlu下\n4号线yishanlu上，zhongshangongyuan下”

​	**不可到达。**如果站点暂时封闭或者不存在等情况则不可到达。

​	**如果多条路线均最短，则都输出。**如上例，3号和4号线都可以到达zhongshangongyuan，因此输出了两条路线。

### 1.2.6 用户界面

  \- 系统应提供一个简洁直观的菜单，使用户能够轻松输入、修改和查询地铁线路信息。

## 1.3 进阶功能

### 1.3.1 时间权重设置

   \- 系统应支持为地铁线路的各站之间以及换乘站设置时间权重。

   \- 输入线路信息时，各站点间的默认时间权重为1单位时间。用户可以修改特定站点间的时间权重。例如，输入 "9 16 17 3" 表示地铁9号线从第16站到第17站的行程需要3个单位时间，其中的站点编号也可以用站名代替，例如输入“9 yishanlu xujiahui 3”表示9号线从yishanlu到xujiahui需要3个单位时间。下同。

   \- 用户可以通过输入特定的格式来设置换乘站的时间权重，如 "3 5 9 16 8"，表示从地铁3号线的第5站换乘到地铁9号线的第16站需要8个单位时间。

### 1.3.2 多条件路线查询

   \- 允许用户选择查询时间最短或换乘次数最少的条件来查询路线。

   \- 系统将根据用户选择的条件提供最多3条最优路线。

### 1.3.3 线路和换乘信息的存储与读取

   \- 系统必须具备将所有线路信息、站点间的时间权重以及换乘站的时间权重保存到文件的能力。

   \- 当程序下次启动时，系统应能够从文件中读取并恢复这些信息，确保用户能够继续使用之前设置的线路和权重信息。

### 1.3.4 用户界面增强

   \- 用户界面应提供直观的输入选项，使用户能够轻松设置和修改时间权重。

   \- 界面应清晰展示路线查询的条件选择（时间最短或换乘最少），并能够展示查询结果的路线列表。

## 1.4 技术要求

  \- 系统应具备良好的数据结构设计，以支持高效的数据存储和查询操作。

  \- 系统应具备错误处理机制，能够处理用户输入错误或不合理的请求。例如要设置9号线第18站到第20站的行程需要5个单位时间，则需提示错误，因为仅能设置相邻站的权重。

# 2 概要

## 2.1 基本功能完成情况

| 功能         | 完成情况 |
| :----------- | -------- |
| 线路信息输入 | √        |
| 换成信息输入 | √        |
| 线路信息修改 | √        |
| 线路查询功能 | √        |
| 路线查询功能 | √        |
| 用户界面     | √        |

## 2.2 进阶功能完成情况

| 功能                       | 完成情况 |
| :------------------------- | -------- |
| 时间权重设置               | √        |
| 多条件路线查询             | √        |
| 线路与换乘信息的存储和读取 | √        |
| 用户界面增强               | √        |



## 2.3 项目目录结构

```
SubwaySystem/
│
├── data/					# 数据存储文件json
│   └── data.json
│
├── data_management/
│   ├── __init__.py
│   ├── data_io.py           # 数据加载和保存
│   │	├── load_data
│   │	└── save_data
│   └── data_operations.py   # 数据操作，如添加线路、站点等
│   	├── add_line
│   	├── get_line
│   	├── build_graph
│   	└── get_data
│
├── user_interface/
│   ├── __init__.py
│   ├── main_window.py       # 设置主窗口和菜单
│   │	├── setup_main_window
│   │	├── setup_path_query_window
│   │	└── query_line_info
│   └── dialogs.py           # 弹窗和其他用户输入界面
│   	├── add_line_window
│   	├── view_transfers
│   	├── update_canvas_on_select
│   	└── show_transfers
│
├── interaction_handlers/
│   ├── __init__.py
│   ├── event_handlers.py    # 事件处理，如按钮点击、右键菜单等
│   │	└── on_right_click
│   └── command_functions.py # 具体执行的命令函数，如添加线路、删除站点
│   	├── add_neighboring_station
│   	├── delete_station
│   	├── toggle_station_status
│   	├── add_transfer
│   	├── delete_transfer
│   	├── submit_new_line
│   	├── update_line_dropdown
│   	└── modify_path
│
├── pathfinding/
│   ├── __init__.py
│   └── shortest_path.py     # 最短路径计算相关函数
│   	├── calculate_shortest_time_path
│   	├── calculate_least_transfers_path
│   	└── show_path_results
│
└── utils/
    ├── __init__.py
    └── visualization.py     # 用于绘制线路图等可视化功能
	   	├── draw_line
 	   	└── exit_application
```

## 2.4 模块和函数分布

### data_management 模块

- **data_io.py**
  - `load_data`
    - 调用：`save_data`
    - 功能：加载数据，如果数据文件不存在，则创建新文件并保存初始化数据。
  - `save_data`
    - 调用：无直接调用其他函数，但会被 `load_data` 调用。
    - 功能：保存当前数据到JSON文件，确保数据的持久化存储。

- **data_operations.py**
  - `add_line`
    - 调用：`save_data` (通过其他函数间接调用)
    - 功能：添加新的地铁线路。
  - `get_line`
    - 功能：根据线路ID获取线路数据。
  - `build_graph`
    - 功能：构建地铁网络图，包括站点和换乘的权重处理。
  - `get_data`
    - 功能：返回当前加载的地铁数据。

### user_interface 模块

- **main_window.py**
  - `setup_main_window`
    - 功能：设置主窗口界面，初始化界面布局和基础交互组件。
  - `setup_path_query_window`
    - 功能：设置路径查询窗口，提供最短时间或最少换乘路径查询选项。
  - `query_line_info`
    - 调用：`draw_line`
    - 功能：根据用户选择的线路显示相关信息和线路图。

- **dialogs.py**
  - `add_line_window`
    - 调用：`submit_new_line`
    - 功能：创建添加新线路的窗口，并处理用户输入。
  - `view_transfers`
    - 功能：显示特定站点的所有换乘情况。
  - `update_canvas_on_select`
    - 功能：根据用户在列表中的选择更新画布显示。
  - `show_transfers`
    - 功能：展示一个站点的换乘详细信息。

### interaction_handlers 模块

- **event_handlers.py**
  - `on_right_click`
    - 调用：`add_neighboring_station`, `delete_station`, `toggle_station_status`, `modify_path`, `view_transfers`
    - 功能：处理用户的右键点击事件，显示操作菜单。

- **command_functions.py**
  - `add_neighboring_station`
    - 调用：`save_data`, `draw_line`
    - 功能：添加邻近站点，并更新数据。
  - `delete_station`
    - 调用：`save_data`, `draw_line`
    - 功能：删除站点，并更新画布。
  - `toggle_station_status`
    - 调用：`save_data`, `draw_line`
    - 功能：更改站点的开放或关闭状态。
  - `add_transfer`
    - 调用：`save_data`, `draw_line`
    - 功能：添加换乘站点。
  - `delete_transfer`
    - 调用：`save_data`, `draw_line`
    - 功能：删除换乘站点。
  - `submit_new_line`
    - 调用：`add_line`, `save_data`, `update_line_dropdown`
    - 功能：提交新线路的创建请求。
  - `update_line_dropdown`
    - 功能：更新线路选择的下拉菜单。
  - `modify_path`
    - 调用：`save_data`, `draw_line`
    - 功能：修改站点间的权重。

### pathfinding 模块

- **shortest_path.py**
  - `calculate_shortest_time_path`
    - 功能：计算最短时间路径。
  - `calculate_least_transfers_path`
    - 功能：计算最少换乘路径。
  - `show_path_results`
    - 功能：展示路径查询结果。

### utils 模块

- **visualization.py**
  - `draw_line`
    - 功能：在画布上绘制线路图。
  - `exit_application`
    - 功能：退出应用程序。

# 3 设计实现

## 3.1 存储结构设计

### 3.1.1 json文件

数据文件使用 JSON 格式，用来存储地铁线路和站点的信息，以及站点间的换乘关系。

```json
{
    "lines": [
        {
            "lineID": "1",
            "lineName": "一号线",
            "stations": [
                {
                    "stationID": "1",
                    "stationName": "人民广场",
                    "lineID": "1",
                    "status": "open",
                    "nextWeight": 10
                }
            ]
        },
        {
            "lineID": "9",
            "lineName": "九号线",
            "stations": [
                {
                    "stationID": "1",
                    "stationName": "漕河泾开发区",
                    "lineID": "9",
                    "status": "open",
                    "nextWeight": 1
                },
                 ……（省略部分）……
                {
                    "stationID": "7",
                    "stationName": "打浦桥",
                    "lineID": "9",
                    "status": "open",
                    "nextWeight": null
                }
            ]
        }
    ],
    "transfers": [
        {
            "fromLine": "1",
            "fromStation": "徐家汇",
            "toLine": "9",
            "toStation": "徐家汇",
            "nextWeight": 10
        },
        {
            "fromLine": "9",
            "fromStation": "徐家汇",
            "toLine": "1",
            "toStation": "徐家汇",
            "nextWeight": 10
        }
    ]
}
```

####  主要组成部分

1. **lines**：这是一个数组，包含了多条地铁线路的详细信息。
2. **transfers**：这是一个数组，包含了换乘站点之间的关系及权重。

#### 线路(Line)数据结构

每条线路由以下字段组成：

- **lineID**：线路的唯一标识符。
- **lineName**：线路的名称。
- **stations**：该线路上的所有站点的数组。

#### 站点(Station)数据结构

每个站点具有以下属性：

- **stationID**：站点的唯一标识符。
- **stationName**：站点名称。
- **lineID**：站点所属的线路ID。
- **status**：站点的状态（"open" 表示开放，"closed" 表示关闭）。
- **nextWeight**：到下一个站点的权重（时间或距离）。最后一个站点的 `nextWeight` 通常为 `null` 或不提供，表示没有下一个站点。

#### 换乘(Transfer)数据结构

换乘关系定义了从一个线路的站点到另一个线路站点的换乘信息：

- **fromLine**：起始线路ID。
- **fromStation**：起始站点名称。
- **toLine**：目标线路ID。
- **toStation**：目标站点名称。
- **nextWeight**：换乘所需的权重（可能是时间或其他度量）。

#### 特殊情况处理

- **封闭站点**：数据中部分站点的状态为 "closed"，表示这些站点目前不对公众开放。这会影响路径计算和图的构建。
- **换乘站点的权重**：在 `transfers` 数组中定义了换乘站点之间的权重，这对于计算最短或最优路径非常重要。

#### 示例分析

1. **一号线**（Line ID: 1）从人民广场到锦江乐园，共有10个站点，部分站点如常熟路和徐家汇目前处于封闭状态。
2. **九号线**（Line ID: 9）从漕河泾开发区到打浦桥，共有7个站点，其中徐家汇站点也是封闭的。
3. **换乘信息**：在徐家汇可以从一号线换乘到九号线，反之亦然，换乘权重为10。



### 3.1.2 数据存储与读取函数

```py
def load_data():
    global data
    if not os.path.exists(data_path):
        save_data()  # 如果文件不存在，则创建一个新文件
    else:
        try:
            with open(data_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            messagebox.showerror("加载错误", f"无法解析数据文件: {e}")
            data = {"lines": [], "transfers": []}  # 如果文件损坏，初始化为空数据结构
```

```python
def save_data():
    global data
    try:
        os.makedirs(os.path.dirname(data_path), exist_ok=True)  # 确保目录存在
        # 在保存前按线路ID排序
        data['lines'].sort(key=lambda line: int(line['lineID']))
        with open(data_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            # messagebox.showinfo("保存数据", "数据已成功保存！")
    except Exception as e:
        messagebox.showerror("保存错误", f"无法保存数据: {e}")
```



## 3.2 主界面设置

![image-20240703132923491](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703132923491.png)

界面设置通过使用 Python 的 tkinter 库实现，它为地铁路线管理系统提供了一个图形用户界面（GUI）。

```py
def setup_main_window(root):
    canvas = tk.Canvas(root, width=800, height=300)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, fill=tk.X)

    line_var = tk.StringVar(value='请选择线路')
    # 注意：初始化下拉菜单时先不添加任何实际选项
    line_menu = tk.OptionMenu(frame, line_var, '请选择线路')
    line_menu.pack(side=tk.LEFT, padx=5, pady=5)

    # 确保所有必要的 UI 组件已经创建并存储后，再更新下拉菜单
    update_line_dropdown(line_menu, line_var)  # 更新下拉菜单

    btn_query_line = tk.Button(frame, text="查询线路", command=lambda: query_line_info(canvas, line_var, line_menu))
    btn_query_line.pack(side=tk.LEFT, padx=5, pady=5)

    # 添加线路按钮
    btn_add_line = tk.Button(frame, text="添加线路", command=lambda: add_line_window(line_menu, line_var))
    btn_add_line.pack(side=tk.LEFT, padx=5, pady=5)

    # 新增查询最短时间路径按钮
    btn_query_shortest_time = tk.Button(frame, text="查询最短路径",
                                        command=lambda: setup_path_query_window(get_data()))
    btn_query_shortest_time.pack(side=tk.LEFT, padx=5, pady=5)

    btn_exit = tk.Button(frame, text="退出", command=exit_application)
    btn_exit.pack(side=tk.LEFT, padx=5, pady=5)
```

这个函数负责设置主窗口的基本布局和核心交互组件：

1. **Canvas**：
   - 用于绘制和显示地铁线路图。
   - 尺寸设为宽800像素，高300像素，这提供了足够的空间来视觉化展示地铁线路。

2. **Frame**：
   - 作为按钮和下拉菜单的容器，位于窗口的顶部，并填充整个窗口的宽度。

3. **Line Dropdown Menu (`line_menu`)**：
   - 用于选择地铁线路，初始未添加实际选项，选项通过 `update_line_dropdown` 函数动态加载。

4. **Buttons**：
   - `btn_query_line`：查询选中的线路并在画布上显示。
   - `btn_add_line`：打开添加新线路的窗口。
   - `btn_query_shortest_time`：打开查询最短路径的窗口。
   - `btn_exit`：退出应用程序。

## 3.3 主界面功能

![image-20240703132939285](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703132939285.png)

### 3.3.1 查询线路

#### （1）线路信息查询 `query_line_info`

```py
def query_line_info(canvas, line_var, line_menu):
    try:
        # 获取下拉菜单的当前选项
        selected_line_name = line_var.get()
        print(f"Selected Line Name: {selected_line_name}")  # 调试输出选中的线路名称

        # 获取所有线路选项（假设这些选项是在 setup_main_window 中设置的）
        line_options = [(line['lineName'], line['lineID']) for line in get_data()['lines']]
        print(f"Line Options: {line_options}")  # 调试输出所有线路选项

        # 根据选中的线路名称查找对应的线路 ID
        line_id = next((line_id for line_name, line_id in line_options if line_name == selected_line_name), None)
        print(f"Line ID: {line_id}")  # 调试输出找到的线路 ID

        if line_id is not None:
            # 如果找到了线路 ID，继续处理（例如绘制线路图）
            line = get_line(line_id)
            if line:
                draw_line(canvas, line, get_data(), line_menu, line_var)
            else:
                messagebox.showerror("Error", "Line not found.")
        else:
            messagebox.showerror("Error", "Invalid line selection.")
    except Exception as e:
        # 错误处理
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
```

当用户选择一个线路并点击查询按钮时，此函数被调用：

- 获取并验证用户选择的线路。
- 调用 `draw_line` 函数在画布上绘制所选线路。

#### （2）绘制路线图 `draw_line`

这个函数负责在画布上绘制选定的线路图：

- 对于每个站点，根据其是否为换乘站以及是否关闭来改变其显示样式。
- 站点之间的连线显示权重值（如果存在）。
- 使用了颜色、线段、标注来使得图片绘制更加直观。

```python
def draw_line(canvas, line, data, line_menu, line_var):
    if not line:
        return

    canvas.delete("all")  # 清空画布准备新的绘图

    # 显示线路名称在画布顶部
    canvas.create_text(400, 20, text=f"当前线路：{line['lineName']}", font=('Helvetica', 10, 'bold'))

    start_x, start_y = 50, 50  # 初始化起始位置
    x, y = start_x, start_y
    step_x, step_y = 100, 50  # 站点间水平和垂直的距离
    max_x = canvas.winfo_width() - 100  # 避免溢出画布的最大x位置
    direction = 1  # x方向移动，1向右，-1向左
    last_x, last_y = x, y  # 用于追踪上一个站点的位置，以便在拐弯处连接线路

    for i, station in enumerate(line['stations']):
        # 判断是否为换乘站
        is_transfer = any(t['fromStation'] == station['stationName'] or t['toStation'] == station['stationName'] for t in data['transfers'])

        # 绘制站点为一个圆形，如果是换乘站则用不同颜色
        station_id = f"station_{station['stationName']}"
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red" if is_transfer else "blue", outline="black", tags=(station_id,))
        canvas.create_text(x, y + 20, text=station['stationName'])
        canvas.tag_bind(station_id, "<Button-3>",
                        lambda event, s=station: on_right_click(event, s, canvas, data, line['lineID'], line_menu, line_var))

        # 如果站点状态是封闭的，则绘制叉号
        if station.get('status') == 'closed':
            canvas.create_line(x - 12, y - 12, x + 12, y + 12, fill="black", width=2)
            canvas.create_line(x + 12, y - 12, x - 12, y + 12, fill="black", width=2)

        # 在拐弯前连线到当前站点
        if i > 0:
            canvas.create_line(last_x, last_y, x, y, fill="gray")
            if 'nextWeight' in line['stations'][i - 1]:  # Check if the previous station has a weight to the current station
                mid_x, mid_y = (last_x + x) / 2, (last_y + y) / 2
                canvas.create_text(mid_x, mid_y, text=str(line['stations'][i - 1]['nextWeight']), fill="black", font=('Helvetica', 10))

        # 计算下一个站点的x和y位置，并更新last_x, last_y为当前站点位置
        last_x, last_y = x, y
        next_x = x + direction * step_x
        if next_x > max_x or next_x < start_x:
            # 如果下一个x位置超出界限，则换行并反转方向
            y += step_y
            direction *= -1
            x += direction * step_x
        else:
            x = next_x  # 继续同方向移动
```



### 3.3.2 添加线路

![image-20240703135000748](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703135000748.png)

![image-20240703135012621](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703135012621.png)

![image-20240703135022940](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703135022940.png)

#### （1）创建添加新线路的窗口 `add_line_window`

```py
# 创建添加新线路的窗口，包括输入字段和提交按钮
def add_line_window(line_menu, line_var):
    window = Toplevel()
    window.title("添加新线路")


    Label(window, text="线路ID:").pack()
    line_id_entry = Entry(window)
    line_id_entry.pack()

    Label(window, text="线路名称:").pack()
    line_name_entry = Entry(window)
    line_name_entry.pack()

    Label(window, text="站点（使用空格分隔）:").pack()
    stations_entry = Entry(window)
    stations_entry.pack()

    # 确保传递 line_menu 和 line_var 到提交函数
    submit_btn = Button(window, text="提交", command=lambda: submit_new_line(
        line_id_entry.get(), line_name_entry.get(), stations_entry.get(), window, line_menu, line_var))
    submit_btn.pack()
```

此函数使用 tkinter 的 `Toplevel` 创建一个新的顶层窗口，用于输入新线路的相关信息：

- **窗口设置**:
  - 使用 `Toplevel()` 创建一个新窗口，与主窗口平行。
  - `window.title("添加新线路")` 设置窗口标题。

- **输入字段**:
  - **线路ID**：用户输入新线路的唯一标识符。
  - **线路名称**：用户输入新线路的名称。
  - **站点列表**：用户输入新线路的所有站点名称，站点之间用空格分隔。

- **提交按钮**:
  - 按钮触发 `submit_new_line` 函数，传递用户输入的线路ID、线路名称和站点列表，以及当前窗口和下拉菜单的状态。

#### （2）提交新线路数据处理 submit_new_line`

```python
# 处理添加新线路
def submit_new_line(line_id, line_name, stations, window, line_menu, line_var):
    if line_menu is not None:
        update_line_dropdown(line_menu, line_var)
    else:
        messagebox.showerror("错误", "线路菜单未正确初始化。")

    if not line_id.strip() or not line_name.strip() or not stations.strip():
        messagebox.showerror("输入错误", "所有字段均为必填项，请确保填写所有信息。")
        return

    stations_list = re.split(r'[ ,，]+', stations.strip())
    success = add_line(line_id, line_name, stations_list)
    if success:
        window.destroy()
        save_data()  # 添加成功后保存数据
        messagebox.showinfo("成功", "新线路添加成功。")
        update_line_dropdown(line_menu, line_var)  # 更新下拉列表
    else:
        # 如果添加失败（例如ID重复），保留窗口开启，允许用户更正
        pass

```

此函数处理从 `add_line_window` 窗口收集到的数据，并尝试将新线路添加到系统中：

- **输入验证**:
  - 检查 `line_menu` 是否已正确初始化。
  - 验证线路ID、线路名称和站点列表是否均已填写，如果有字段为空，则显示错误消息并终止操作。

- **站点数据处理**:
  - 使用正则表达式 `re.split(r'[ ,，]+', stations.strip())` 分割用户输入的站点字符串，支持逗号或空格作为分隔符，以创建站点列表。

- **调用添加线路函数** (`add_line`):
  - 如果添加成功，关闭输入窗口，保存数据，并通过 `messagebox.showinfo` 显示成功消息。
  - 调用 `update_line_dropdown` 更新下拉菜单，反映新增的线路。
  - 如果添加失败（例如，如果存在重复的线路ID），则不关闭输入窗口，允许用户更正并重新提交。

### 3.3.3 查询最短路径

![image-20240703135412082](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703135412082.png)

![image-20240703135355115](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703135355115.png)

#### （1）用户交互窗口

```python
def setup_path_query_window(data):
    window = tk.Toplevel()
    window.title("查询路径选项")

    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    # 创建变量和下拉菜单
    start_line_var = tk.StringVar(window)
    start_station_var = tk.StringVar(window)
    end_line_var = tk.StringVar(window)
    end_station_var = tk.StringVar(window)
    query_type_var = tk.StringVar(window, value='最短时间')

    # 线路选择下拉菜单
    start_line_menu = tk.OptionMenu(frame, start_line_var, *(line['lineName'] for line in data['lines']))
    start_line_menu.grid(row=0, column=1, padx=10, pady=10)
    end_line_menu = tk.OptionMenu(frame, end_line_var, *(line['lineName'] for line in data['lines']))
    end_line_menu.grid(row=1, column=1, padx=10, pady=10)

    # 站点选择下拉菜单，初始为空
    start_station_menu = tk.OptionMenu(frame, start_station_var, "选择起始站")
    start_station_menu.grid(row=0, column=3, padx=10, pady=10)
    end_station_menu = tk.OptionMenu(frame, end_station_var, "选择目的站")
    end_station_menu.grid(row=1, column=3, padx=10, pady=10)

    # 查询类型选择下拉菜单
    query_type_menu = tk.OptionMenu(frame, query_type_var, '最短时间', '最少换乘')
    query_type_menu.grid(row=2, column=1, padx=10, pady=10)

    # 更新站点下拉菜单的函数
    def update_station_menu(line_var, station_var, station_menu):
        selected_line = next((line for line in data['lines'] if line['lineName'] == line_var.get()), None)
        station_var.set('')
        menu = station_menu["menu"]
        menu.delete(0, 'end')
        for station in selected_line['stations']:
            menu.add_command(label=station['stationName'], command=lambda value=station['stationName']: station_var.set(value))

    # 绑定更新函数到线路变量
    start_line_var.trace('w', lambda *args: update_station_menu(start_line_var, start_station_var, start_station_menu))
    end_line_var.trace('w', lambda *args: update_station_menu(end_line_var, end_station_var, end_station_menu))

    # 查询按钮
    def execute_query():
        start_station = start_station_var.get()
        end_station = end_station_var.get()
        query_type = query_type_var.get()  # 确保有一个变量来获取查询类型
        graph = build_graph(data)

        if query_type == 'time':
            path, total_time, transfers = calculate_shortest_time_path(start_station, end_station, graph)
        else:
            path, total_time, transfers = calculate_least_transfers_path(start_station, end_station, graph)

        show_path_results(path, total_time, data)  # 调整函数调用以传递额外的参数
        window.destroy()

    query_button = tk.Button(frame, text="transfers", command=execute_query)
    query_button.grid(row=3, column=1, columnspan=2, pady=20)

    window.mainloop()
```

通过 Tkinter 创建的交互式窗口实现了一个用于查询路径的用户界面，允许用户选择起始线路、起始站点、目的线路、目的站点，以及查询类型（最短时间或最少换乘）

**用户交互设计**

1. **窗口和布局**：
   - 使用 `Toplevel()` 创建一个新窗口，这允许该查询窗口独立于主窗口存在。
   - `Frame` 作为主要的容器，用于组织和定位界面元素。

2. **下拉菜单**：
   - **线路选择**：两个下拉菜单允许用户选择起始线路和目的线路。这些菜单使用列表推导从提供的数据中提取线路名称。
   - **站点选择**：两个初始为空的下拉菜单用于选择起始站和目的站。这些菜单在用户选择线路后动态更新。

3. **动态更新站点列表**：
   - 使用一个内部函数 `update_station_menu` 来更新站点下拉菜单。这个函数根据用户选择的线路更新站点选项。
   - 使用 `trace` 方法绑定变量的更改事件，当线路选择变化时自动触发更新函数。

4. **查询类型选择**：
   - 另一个下拉菜单允许用户选择查询类型：最短时间或最少换乘。

5. **查询执行按钮**：
   - 一个按钮触发路径查询的执行。按钮点击时，函数读取所有用户输入，构建图，执行查询，显示结果，并关闭查询窗口。

**函数细节**

- **菜单项命令的lambda绑定**：使用lambda表达式来绑定命令时，需要注意捕获正确的变量值。在你的代码中，lambda通过闭包正确地引用了循环变量，这在Python中有时会出错，但在这种情况下是安全的。

- **查询执行逻辑**：
  - 根据用户选择的查询类型，调用 `calculate_shortest_time_path` 或 `calculate_least_transfers_path` 函数。
  - 这两个函数都使用构建的图来查找路径。
  - 查询结果通过 `show_path_results` 函数展示，并在显示结果后销毁窗口。

#### （2）图结构的建立 build_graph

```python
def build_graph(data):
    """
    Build a graph representation of the subway network considering station closures and time weights.
    :param data: The data dictionary containing all lines, stations, and transfers with weights
    :return: A dictionary representing the graph of the network, where keys are station names, and values are dicts of neighboring stations with weights.
    """
    graph = {}
    # 首先处理线路内的站点
    for line in data['lines']:
        previous_station = None
        for station in line['stations']:
            if station['status'] == 'closed':
                previous_station = None  # 当前站点封闭，断开与前一个站点的连接
                continue
            if station['stationName'] not in graph:
                graph[station['stationName']] = {}

            if previous_station and previous_station['status'] == 'open':  # 确保前一个站点是开放的
                # 使用时间权重连接前一个站点和当前站点
                weight = station.get('nextWeight', None)  # 获取权重，如果没有指定则默认为None或其他适当的默认值
                if weight is not None:  # 仅当有有效的权重时添加连接
                    graph[previous_station['stationName']][station['stationName']] = weight
                    graph[station['stationName']][previous_station['stationName']] = weight
            previous_station = station  # 更新前一个站点为下次迭代准备

    # 处理换乘，确保涉及的站点都是开放的，并添加权重
    for transfer in data['transfers']:
        from_station_info = next((s for l in data['lines'] for s in l['stations'] if s['stationName'] == transfer['fromStation'] and s['lineID'] == transfer['fromLine']), None)
        to_station_info = next((s for l in data['lines'] for s in l['stations'] if s['stationName'] == transfer['toStation'] and s['lineID'] == transfer['toLine']), None)
        if from_station_info and to_station_info and from_station_info['status'] == 'open' and to_station_info['status'] == 'open':
            weight = transfer.get('nextWeight', None)  # 获取换乘的权重
            if weight is not None:  # 确保权重有效
                graph[from_station_info['stationName']][to_station_info['stationName']] = weight
                graph[to_station_info['stationName']][from_station_info['stationName']] = weight

    return graph
```

此段代码从存储的JSON数据中构建一个图数据结构，用于表示整个地铁网络。

**数据结构**

这段代码构建的是一个**无向加权图**，它用于表示地铁站之间的连接和权重。图中的节点是地铁站，边是站点间的直接连接，边的权重表示从一个站点到另一个站点的成本。

- **节点（Vertex）**：地铁站点，用站名表示。
- **边（Edge）**：站点之间的连接。如果站点A和站点B之间有直接路径，则A的字典中将包含一个指向B的条目，其值为A到B的权重；反之亦然。
- **权重（Weight）**：通常表示从一个站点到另一个站点的时间或者距离。在本例中，权重存储在 `nextWeight` 属性中。

**代码功能解析**

1. **初始化图**：
   - 创建一个空字典 `graph`，用来存储图的数据结构，其中键是站名，值是另一个字典，表示邻接站点及其连接权重。

2. **处理线路内的站点**：
   - 遍历每条线路的每个站点。
   - 对于每个站点，如果它是开放的（`status` 为 'open'），则检查是否有前一个站点存在且也是开放的。如果是，创建两个方向的连接，并赋予相应的权重。
   - 如果站点关闭（`status` 为 'closed'），则跳过此站点，并且不与前一个站点建立连接。

3. **处理换乘**：
   - 遍历所有定义的换乘关系。
   - 对于每个换乘，确定涉及的两个站点都是开放的。如果是，添加双向连接，并设定权重。

4. **返回图**：
   - 完成图的构建后，返回 `graph` 字典。

#### （3）最短时间路径查询  `calculate_shortest_time_path`

```python
def calculate_shortest_time_path(start, end, graph):
    if start not in graph or end not in graph:
        return None, 0

    queue = [(0, start, [start])]
    visited = {}
    while queue:
        current_time, current, path = heapq.heappop(queue)

        if current in visited and visited[current] <= current_time:
            continue
        visited[current] = current_time

        if current == end:
            transfers = sum(1 for i in range(len(path) - 1) if path[i].split('_')[0] != path[i + 1].split('_')[0])
            return path, current_time, transfers

        for neighbor, time in graph[current].items():
            if neighbor not in visited or visited[neighbor] > current_time + time:
                heapq.heappush(queue, (current_time + time, neighbor, path + [neighbor]))

    return None, 0, 0
```

使用的是 **Dijkstra算法的变种**，它通过使用优先队列（通常实现为最小堆）来保证总是先处理当前已知最短时间路径上的站点。

- **图结构**：图的节点代表地铁站，边代表站点之间的直接连接，边的权重是时间成本。
- **实现细节**：
  - 使用一个优先队列（通过 `heapq` 模块实现的堆）来存储待处理的站点和它们的累积旅行时间。
  - 使用字典 `visited` 来记录每个站点的最短访问时间，避免重复处理。
  - 每次从队列中取出累积时间最短的站点进行处理，检查它的邻接站点，并更新邻接站点的最短时间。
  - 追踪路径，以便在找到目的地时返回完整的路线和所需时间。
  - 计算换乘次数，这是通过比较路径上连续站点的线路ID来完成的。

#### （4）最少换乘次数路径查询  `calculate_least_transfers_path`

```python
def calculate_least_transfers_path(start, end, graph):
    if start not in graph or end not in graph:
        return None, 0, 0

    queue = deque([(start, [start])])
    visited = {}
    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited[current] = path

        if current == end:
            total_time = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
            transfers = sum(1 for i in range(len(path) - 1) if path[i].split('_')[0] != path[i + 1].split('_')[0])
            return path, total_time, transfers

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, 0, 0
```

采用了 **广度优先搜索 (BFS)**，适合于找到换乘次数最少的路径。它使用队列来实现层次遍历，确保先处理的路径具有较少的换乘次数。

- **图结构**：同样是节点代表站点，边代表直接连接。
- **实现细节**：
  - 使用一个队列来存储当前待处理的路径和站点。
  - 与上述方法相似，使用 `visited` 字典来记录访问过的站点，防止重复处理。
  - 从队列中顺序取出站点进行处理，探索所有邻接站点，并将新的路径加入队列。
  - 与最短时间路径算法不同，此算法关注的是最小化路径上的换乘次数，而不是时间。
  - 当到达终点站时，计算整条路径的总时间和换乘次数。

#### （5）结果展示 show_path_results

```python
def show_path_results(path, total_time, data):
    if not path:
        result = "不可到达。"
    else:
        result = "路线详情：\n"
        previous_line = None
        station_count = 0  # 用于计数经过的站点
        details = []  # 用于存储路线的详细信息
        transfers = 0  # 用于计数换乘次数

        for i in range(len(path) - 1):
            current_station = path[i]
            next_station = path[i + 1]
            # 查找当前站点和下一站点所在的线路名称
            current_line = next((line['lineName'] for line in data['lines'] if
                                 any(s['stationName'] == current_station for s in line['stations']) and
                                 any(s['stationName'] == next_station for s in line['stations'])), None)
            if previous_line is None:
                # 初始化时设置起始站和线路信息
                previous_line = current_line
                details.append(f"从 {current_station} (乘坐 {current_line} ) 出发，")
                station_count = 1
            elif previous_line == current_line:
                station_count += 1  # 同一条线路上，累加站点数量
            else:
                # 当换乘到不同的线路时，记录前一条线路的信息
                details.append(f"经过 {station_count} 站在 {current_station} 换乘至 {current_line}")
                station_count = 1  # 重置站点计数器
                transfers += 1  # 增加换乘次数
                previous_line = current_line

        # 添加最后一条线路的信息
        details.append(f"经过 {station_count} 站在 {path[-1]} 下车。")

        result += " ".join(details) + f"\n总时间: {total_time} 分钟\n换乘次数: {transfers}"

    tk.messagebox.showinfo("查询结果", result)
```

1. **空路径处理**：
   - 如果 `path` 为空，这意味着没有可达的路径从起点到终点，函数立即返回一个消息提示“不可到达。”，这在路线被封锁或断开时非常有用。
2. **初始化变量**：
   - `previous_line`：用于跟踪当前遍历的站点所在的线路，帮助检测何时发生换乘。
   - `station_count`：计数器，用于统计在同一线路上通过的站点数量。
   - `details`：列表，用于存储整个行程的详细描述。
   - `transfers`：换乘次数计数器。
3. **路径遍历**：
   - 遍历 `path` 中的每个站点，除了最后一个站点，因为每次处理都涉及当前站点到下一个站点的转移。
   - 对于路径中的每一对相邻站点，找出它们所在的线路。这通过检查数据中的线路和站点列表完成。
   - 如果是路径中的第一对站点，初始化起始站和线路信息。
   - 如果当前站点和下一站点在同一条线路上，累加 `station_count`。
   - 如果发生换乘（当前站点和下一站点在不同的线路上），记录换乘，并在结果详情中添加换乘信息，重置 `station_count` 并更新 `previous_line`。
4. **添加最后一条线路的信息**：
   - 由于最后一站不需要与下一站比较，单独处理，添加如何到达最终站点的信息。
5. **结果拼接和展示**：
   - 将行程的详细信息列表 `details` 拼接成一个字符串，并加上总时间和换乘次数的统计信息。
   - 使用 `tk.messagebox.showinfo` 显示最终的查询结果，这使得信息展示直观且友好。

## 3.4 站点交互菜单栏

使用 tkinter 创建了一个右键菜单，使用户能够对选定的站点执行多种操作。这增加了交互性，并允许用户直接在图形界面上管理站点。

### 3.4.1 菜单栏设置 on_right_click

![image-20240703133035810](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703133035810.png)

```python
def on_right_click(event, station, canvas, data, line_id, line_menu, line_var):
    from interaction_handlers.command_functions import add_neighboring_station, delete_station, toggle_station_status, modify_path
    from user_interface.dialogs import view_transfers

    # 创建一个简单的右键菜单
    menu = tk.Menu(canvas, tearoff=0)
    menu.add_command(label="增加邻近站点",
                     command=lambda: add_neighboring_station(station, data, canvas, line_id, line_menu, line_var))
    menu.add_command(label="删除该站点",
                     command=lambda: delete_station(station, data, canvas, line_id, line_menu, line_var))
    menu.add_command(label="查看换乘情况",
                     command=lambda: view_transfers(station, data, canvas, line_menu, line_var))  # 新增查看换乘情况
    menu.add_command(label="修改路径权重", command=lambda: modify_path(station, data, canvas, line_id))  # 新增修改路径权重功能

    if station.get('status') == 'open':
        menu.add_command(label="封闭站点",
                         command=lambda: toggle_station_status(station, data, canvas, line_id, 'closed', line_menu,
                                                               line_var))
    else:
        menu.add_command(label="恢复站点",
                         command=lambda: toggle_station_status(station, data, canvas, line_id, 'open', line_menu,
                                                               line_var))
    menu.post(event.x_root, event.y_root)
```

#### 创建右键菜单

- 使用 `tk.Menu` 创建一个新的菜单实例，`tearoff=0` 参数禁止菜单被独立为一个窗口。
- 菜单与特定的 `canvas` 组件相关联，这意味着菜单将在这个画布上显示。

#### 菜单选项添加

- **增加邻近站点**：添加一个菜单项，当选中时，调用 `add_neighboring_station` 函数以在选中的站点旁边添加一个新站点。
- **删除该站点**：添加一个菜单项，当选中时，调用 `delete_station` 函数以从数据中删除当前选中的站点。
- **查看换乘情况**：添加一个菜单项，当选中时，调用 `view_transfers` 函数以显示当前站点的所有换乘关系。
- **修改路径权重**：添加一个菜单项，当选中时，调用 `modify_path` 函数以调整从当前站点到邻近站点的权重。

#### 状态敏感操作

- 根据站点的当前开放状态（`open` 或 `closed`），菜单会动态添加“封闭站点”或“恢复站点”的选项。
- 这些选项分别调用 `toggle_station_status` 函数来更改站点的状态。

#### 显示菜单

- 使用 `menu.post(event.x_root, event.y_root)` 方法在鼠标右键点击的位置显示菜单。`event.x_root` 和 `event.y_root` 是事件发生时鼠标在屏幕上的位置。

### 3.4.2 增加邻近站点 Add Neighboring Station

![image-20240703134347711](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703134347711.png)

![image-20240703134401961](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703134401961.png)

![image-20240703134424410](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703134424410.png)

![image-20240703134438373](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703134438373.png)

```python
def add_neighboring_station(station, data, canvas, line_id, line_menu, line_var):
    def submit():
        new_station_name = station_name_entry.get()
        position = var.get()
        weight_input = weight_entry.get().strip()

        # Ensure input is not empty
        if not new_station_name.strip():
            messagebox.showerror("Error", "Station name cannot be empty")
            return
        if not weight_input.isdigit():
            messagebox.showerror("Error", "Weight must be a numeric value")
            return
        time_weight = int(weight_input)

        current_line = next((line for line in data['lines'] if line['lineID'] == line_id), None)

        # Check for duplicate station names
        if any(st['stationName'] == new_station_name for st in current_line['stations']):
            messagebox.showerror("Error",
                                 "A station with the same name already exists on this line. Please use a different name.")
            return

        # Find the current station in data and insert the new station based on selected position
        for line in data['lines']:
            for idx, st in enumerate(line['stations']):
                if st['stationName'] == station['stationName']:
                    new_station = {"stationID": str(idx + 1), "stationName": new_station_name, "lineID": line_id,
                                   "status": "open", "nextWeight": time_weight}
                    if position == 'prev':
                        # Adjust time weights accordingly
                        if idx > 0:
                            new_station['nextWeight'] = line['stations'][idx - 1]['nextWeight']
                            line['stations'][idx - 1]['nextWeight'] = time_weight
                        line['stations'].insert(idx, new_station)
                    else:
                        if idx < len(line['stations']) - 1:
                            new_station['nextWeight'] = line['stations'][idx]['nextWeight']
                        line['stations'][idx]['nextWeight'] = time_weight
                        line['stations'].insert(idx + 1, new_station)
                    break

        # Update station IDs
        for line in data['lines']:
            for idx, st in enumerate(line['stations']):
                st['stationID'] = str(idx + 1)
        # Save data
        save_data()
        window.destroy()

        # Redraw the line after data update
        line = get_line(line_id)
        if line:
            draw_line(canvas, line, data, line_menu, line_var)

    window = Toplevel()
    window.title("Add Neighboring Station")

    var = tk.StringVar(value="next")
    tk.Radiobutton(window, text="Add Previous Station", variable=var, value="prev").pack()
    tk.Radiobutton(window, text="Add Next Station", variable=var, value="next").pack()

    Label(window, text="Station Name:").pack()
    station_name_entry = Entry(window)
    station_name_entry.pack()

    Label(window, text="Weight to Next/Previous Station:").pack()
    weight_entry = Entry(window)
    weight_entry.pack()

    Button(window, text="Submit", command=submit).pack()
```

**创建窗口与控件**：

- 使用 `Toplevel()` 创建一个新的顶级窗口。
- 在窗口中设置用于输入站点名称和权重的文本输入框（`Entry`）。
- 使用 `Radiobutton` 提供用户选择新站点添加位置的选项：前一站（`prev`）或后一站（`next`）。

**用户输入验证**：

- 验证站点名称不为空且权重为有效的数字。

**检查站点名称重复**：

- 遍历当前线路的所有站点，确保没有重复的站点名称。

**添加新站点**：

- 根据用户选择的位置（前一站或后一站），计算新站点应插入的位置。
- 调整相邻站点的权重，确保新站点的权重逻辑正确。

**更新站点ID和数据保存**：

- 为确保连续性，重新为所有站点分配 `stationID`。
- 调用 `save_data()` 函数保存更改。

**界面更新**：

- 关闭输入窗口。
- 重新绘制已更新的线路图，以便用户可以立即看到更改结果。

### 3.4.3 删除该站点 Delete Station

```python
# 删除站点
def delete_station(station, data, canvas, line_id, line_menu, line_var):
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
        save_data()
        messagebox.showinfo("删除成功", "站点已删除，并更新了数据。")

        # 更新数据后重新绘制线路
        line = get_line(line_id)
        if line:
            draw_line(canvas, line, data, line_menu, line_var)
        else:
            canvas.delete("all")  # 如果线路被删除，则清空 Canvas
            update_line_dropdown(line_menu, line_var)
```

- 使用户能够删除选定的站点。
- 如果删除站点后某条线路没有剩余站点，则整条线路也会被删除。
- 这对于维护线路或去除不再服务的站点很有用。

**确认删除**：

- 用户触发删除操作后，首先会看到一个确认对话框，询问是否真的要删除该站点。

**处理站点和线路数据**：

- 遍历所有线路，移除指定的站点。
- 如果移除后线路没有剩余站点，整条线路也将被删除。
- 更新剩余站点的 `stationID`，确保连续性和一致性。

**处理换乘关系**：

- 移除所有涉及被删除站点的换乘关系。

**数据保存和界面更新**：

- 调用 `save_data()` 函数保存所有更改。
- 更新图形界面，反映站点和线路的最新状态。

### 3.4.4 查看换乘情况 View Transfers

![image-20240703141536386](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703141536386.png)

```python
def view_transfers(station, data, canvas, line_menu, line_var):
    window = tk.Toplevel()
    window.title(f"换乘情况 - {station['stationName']}")

    window.geometry('300x200')

    # 筛选以当前站点为起点的换乘关系，并按照目的线路ID和目的站点名称排序
    transfers = [t for t in data['transfers'] if
                 t['fromStation'] == station['stationName'] and t['fromLine'] == station['lineID']]
    transfers.sort(key=lambda x: (x['toLine'], x['toStation']))  # 根据目的线路ID和站点名称排序

    listbox = tk.Listbox(window)
    for t in transfers:
        listbox.insert(tk.END, f" {t['fromLine']} ： {t['fromStation']} -> {t['toLine']} ： {t['toStation']} —— {t['nextWeight']}")
    listbox.pack(fill=tk.BOTH, expand=True)

    # 删除和添加换乘站的按钮
    delete_button = tk.Button(window, text="删除该换乘站",
                              command=lambda: delete_transfer(transfers, listbox, data, canvas, station['lineID'], line_menu, line_var))
    delete_button.pack(side=tk.LEFT)
    add_button = tk.Button(window, text="添加换乘站", command=lambda: add_transfer(station, data, canvas, listbox, line_menu, line_var))
    add_button.pack(side=tk.RIGHT)

    # 这里还需要确保更新画布后显示正确的线路
    listbox.bind('<<ListboxSelect>>',
                 lambda event: update_canvas_on_select(event, canvas, data, station['lineID'], line_menu, line_var))
```

为用户提供了一个界面，显示选定地铁站的所有换乘关系。用户可以查看每个换乘的详细信息，包括起始线路、起始站点、目的线路、目的站点以及换乘权重。此外，用户可以通过界面直接删除或添加换乘关系。

#### （1）添加换乘站

![image-20240703141806133](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703141806133.png)

![image-20240703141818218](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703141818218.png)

![image-20240703141825538](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703141825538.png)

![image-20240703141834896](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703141834896.png)

```python
def add_transfer(station, data, canvas, listbox, line_menu, line_var):
    line_id = station['lineID']  # Directly obtain lineID from station data
    transfer_window = tk.Toplevel()
    transfer_window.title("Add Transfer Station")

    main_frame = tk.Frame(transfer_window)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Dropdown menu to select a line, excluding the current station's line
    line_var = tk.StringVar(transfer_window)
    line_options = [line['lineName'] for line in data['lines'] if line['lineID'] != line_id]
    if line_options:
        line_menu = tk.OptionMenu(main_frame, line_var, *line_options)
    else:
        line_menu = tk.OptionMenu(main_frame, line_var, "No available lines")
    line_menu.pack()

    # Dropdown menu for station selection, initially empty
    station_var = tk.StringVar(transfer_window)
    station_menu = tk.OptionMenu(main_frame, station_var, "Select a station")
    station_menu.pack()

    # Entry for weight to and from the transfer station
    Label(main_frame, text="Weight to Transfer Station:").pack()
    weight_entry = tk.Entry(main_frame)
    weight_entry.pack()

    # Function to update the station menu based on the selected line
    def update_station_menu(*args):
        selected_line = next((line for line in data['lines'] if line['lineName'] == line_var.get()), None)
        station_menu['menu'].delete(0, 'end')
        if selected_line:
            for station in selected_line['stations']:
                station_menu['menu'].add_command(label=station['stationName'],
                                                 command=lambda value=station['stationName']: station_var.set(value))
        else:
            station_menu['menu'].add_command(label="No stations", command=lambda: station_var.set("No stations"))

    line_var.trace('w', update_station_menu)

    # Confirm transfer addition
    def confirm_transfer():
        weight = weight_entry.get().strip()
        if not weight.isdigit():
            messagebox.showerror("Error", "Weight must be a numeric value.")
            return
        weight = int(weight)

        to_line = next((line for line in data['lines'] if line['lineName'] == line_var.get()), None)
        to_station_name = station_var.get()
        if to_line and to_station_name:
            new_transfer = {
                "fromLine": line_id,
                "fromStation": station['stationName'],
                "toLine": to_line['lineID'],
                "toStation": to_station_name,
                "nextWeight": weight
            }
            reverse_transfer = {
                "fromLine": to_line['lineID'],
                "fromStation": to_station_name,
                "toLine": line_id,
                "toStation": station['stationName'],
                "nextWeight": weight
            }
            data['transfers'].append(new_transfer)
            data['transfers'].append(reverse_transfer)
            save_data()
            listbox.insert(tk.END, f"新增： {station['stationName']} <-> {to_station_name}")
            transfer_window.destroy()
            # Refresh the canvas to display the update
            line = get_line(line_id)
            if line:
                draw_line(canvas, line, data, line_menu, line_var)

    confirm_button = tk.Button(transfer_window, text="Confirm", command=confirm_transfer)
    confirm_button.pack()


# 删除换乘站点
def delete_transfer(transfers, listbox, data, canvas, line_id, line_menu, line_var):
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
            save_data()
            listbox.delete(index)  # 删除列表中的项
            tk.messagebox.showinfo("删除成功", "换乘关系已删除")

            # 更新数据后重新绘制线路
            line = get_line(line_id)
            if line:
                draw_line(canvas, line, data, line_menu, line_var)
            else:
                canvas.delete("all")  # 如果线路被删除，则清空 Canvas
                update_line_dropdown(line_menu, line_var)

```

**创建用户界面**：

- 使用 `Toplevel()` 创建一个新的顶层窗口，用于输入换乘信息。
- `OptionMenu` 用于选择要换乘到的线路和站点，排除当前站点所在的线路。
- `Entry` 用于输入从当前站点到目的站点的权重。

**用户输入验证**：

- 检查输入的权重是否为有效的数字。

**添加换乘关系**：

- 确定所选线路和站点，并构建新的换乘关系记录。
- 添加这个换乘关系及其反向关系到 `data['transfers']`，确保可以从两个方向进行换乘。

**数据保存和界面更新**：

- 调用 `save_data()` 函数保存更改。
- 将新的换乘关系添加到界面的列表中，让用户立即看到更新的结果。
- 关闭输入窗口。

#### （2）删除换乘站

```python
def delete_transfer(transfers, listbox, data, canvas, line_id, line_menu, line_var):
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
            save_data()
            listbox.delete(index)  # 删除列表中的项
            tk.messagebox.showinfo("删除成功", "换乘关系已删除")

            # 更新数据后重新绘制线路
            line = get_line(line_id)
            if line:
                draw_line(canvas, line, data, line_menu, line_var)
            else:
                canvas.delete("all")  # 如果线路被删除，则清空 Canvas
                update_line_dropdown(line_menu, line_var)
```

**用户选择操作**：

![image-20240703142404917](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703142404917.png)

- 通过 `listbox.curselection()` 获取用户在列表框中选择的项。列表框包含了所有的换乘关系。
- `selected[0]` 提取选择的第一项，这是基于 Tkinter 列表框的工作方式，其中选择返回一个包含索引的元组。

**确认删除操作**：

![image-20240703142416116](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703142416116.png)

- 使用 `tk.messagebox.askyesno` 弹出一个确认对话框，询问用户是否确定要删除选定的换乘关系。这增加了操作的安全性，避免误操作导致数据丢失。

**执行删除**：

- 如果用户确认删除，函数会遍历 `data['transfers']` 列表，通过列表推导移除与选定换乘及其反向关系相匹配的所有条目。
- 这里的匹配条件是检查 `fromStation` 和 `toStation` 是否与选定的换乘关系或其反向关系一致。

**更新界面和数据**：

- 使用 `listbox.delete(index)` 从列表框中移除用户选择的换乘关系，这样用户立即看到操作结果。
- 调用 `save_data()` 函数保存更新后的数据，保证数据的持久性和一致性。

**视觉反馈**：

![image-20240703142430039](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703142430039.png)

![image-20240703142435676](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703142435676.png)

![image-20240703142442960](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703142442960.png)

![image-20240703142451443](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703142451443.png)

- 如果换乘删除成功，通过 `tk.messagebox.showinfo` 提示用户删除成功。
- 重新绘制更新后的地铁线路或在必要时更新线路下拉菜单。

### 3.4.5 修改路径权重

![image-20240703143210323](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143210323.png)

```python
def modify_path(station, data, canvas, line_id):
    window = tk.Toplevel()
    window.title("修改路径权重")

    frame = tk.Frame(window)
    frame.pack(padx=10, pady=10)

    # 获取当前线路信息
    line = next((l for l in data['lines'] if l['lineID'] == line_id), None)
    if not line:
        tk.messagebox.showerror("错误", "线路数据未找到。")
        return

    # 找到当前站点在线路中的索引
    index = next((idx for idx, s in enumerate(line['stations']) if s['stationName'] == station['stationName']), None)
    if index is None:
        tk.messagebox.showerror("错误", "站点未在当前线路中找到。")
        return

    # 单选按钮选择修改前一站或后一站的权重
    direction_var = tk.StringVar(value="next")  # 默认选择“后一站”

    if index > 0:  # 如果不是第一站，允许选择“前一站”
        tk.Radiobutton(frame, text="修改到前一站的权重", variable=direction_var, value="prev").pack(anchor='w')
    if index < len(line['stations']) - 1:  # 如果不是最后一站，允许选择“后一站”
        tk.Radiobutton(frame, text="修改到后一站的权重", variable=direction_var, value="next").pack(anchor='w')

    # 权重输入框
    tk.Label(frame, text="输入新的权重：").pack()
    weight_entry = tk.Entry(frame)
    weight_entry.pack()

    # 提交按钮，更新权重
    def submit_weight_update():
        new_weight = weight_entry.get()
        if not new_weight.isdigit():
            tk.messagebox.showerror("错误", "权重必须为数字。")
            return
        new_weight = int(new_weight)
        if direction_var.get() == "prev" and index > 0:
            line['stations'][index - 1]['nextWeight'] = new_weight
        elif direction_var.get() == "next" and index < len(line['stations']) - 1:
            line['stations'][index]['nextWeight'] = new_weight
        save_data()  # 保存数据
        window.destroy()
        draw_line(canvas, line, data, None, None)  # 重绘线路图

    submit_button = tk.Button(frame, text="提交", command=submit_weight_update)
    submit_button.pack()

    window.mainloop()
```

**创建用户界面**：

- 使用 `Toplevel()` 创建一个新的顶层窗口。
- 在窗口中使用 `Frame` 组织布局，并添加相关控件，如单选按钮、标签、文本输入框和按钮。

**选择修改权重的方向**：

- 使用单选按钮 (`Radiobutton`) 让用户选择是修改到前一站的权重还是后一站的权重。
- 根据当前站点在线路中的位置，确定可选的方向（首站不能选择前一站，末站不能选择后一站）。

**权重输入验证**：

- 用户输入的新权重值必须为有效数字。

**提交并更新数据**：

- 根据用户选择的方向和输入的权重值更新数据模型中的权重。
- 调用 `save_data()` 函数保存数据更改。

**界面更新**：

- 关闭输入窗口。
- 重新绘制已更新的线路图，以便用户可以立即看到更改结果。

### 3.4.6 封闭/恢复站点 Close/Open Station

#### 封闭站点

![image-20240703143246580](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143246580.png)

![image-20240703143255407](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143255407.png)

![image-20240703143303254](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143303254.png)

#### 恢复站点

![image-20240703143329732](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143329732.png)

![image-20240703143338454](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143338454.png)

![image-20240703143346426](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240703143346426.png)



```python
def toggle_station_status(station, data, canvas, line_id, new_status, line_menu, line_var):
    # 更改指定站点的状态
    station['status'] = new_status

    # 找到与此站点有直接换乘关系的所有站点，并更改它们的状态
    for transfer in data['transfers']:
        if transfer['fromStation'] == station['stationName'] and transfer['fromLine'] == line_id:
            # 找到换乘到的站点，并更新状态
            to_station_info = next((s for l in data['lines'] for s in l['stations'] if
                                    s['stationName'] == transfer['toStation'] and s['lineID'] == transfer['toLine']),
                                   None)
            if to_station_info:
                to_station_info['status'] = new_status
        elif transfer['toStation'] == station['stationName'] and transfer['toLine'] == line_id:
            # 找到从哪个站点换乘过来的，并更新状态
            from_station_info = next((s for l in data['lines'] for s in l['stations'] if
                                      s['stationName'] == transfer['fromStation'] and s['lineID'] == transfer[
                                          'fromLine']), None)
            if from_station_info:
                from_station_info['status'] = new_status

    # 保存数据
    save_data()

    # 重新绘制线路图以显示状态更新
    line = get_line(line_id)
    if line:
        draw_line(canvas, line, data, line_menu, line_var)
```

**修改站点状态**：

- 直接在传入的 `station` 字典中修改 `status` 键的值。这一操作立即改变了指定站点的开放或封闭状态。

**更新相关换乘站点状态**：

- 遍历 `data['transfers']` 中所有换乘记录，查找涉及当前站点的所有换乘关系。
- 对于每个相关的换乘，检查它是从当前站点换乘到其他站点，还是从其他站点换乘到当前站点。
- 使用 `next()` 和生成器表达式从 `data['lines']` 中找到对应的站点信息，并更新这些站点的状态。这确保了任何从当前站点直接换乘到的站点或从其他站点换乘到当前站点的状态都会被同步更新。

**数据保存**：

- 调用 `save_data()` 函数将更改持久化，将数据写回到json文件。

**界面更新**：

- 通过调用 `get_line()` 获取当前线路的最新数据。
- 如果线路存在，调用 `draw_line()` 在画布上重新绘制该线路，这样用户界面立即显示出站点状态的更改。

## 3.5 时间复杂度分析

这些函数的时间复杂度分析如下：

### add_neighboring_station

- **时间复杂度**: O(n^2)
- **分析**:
  - 在当前线路中搜索和操作站点的过程，涉及遍历线路和站点列表。
  - 更新站点ID和保存数据都需要遍历站点列表。
  - 所有的遍历操作的复杂度取决于站点数量。

### delete_station

- **时间复杂度**: O(n^2)
- **分析**:
  - 在每条线路中搜索和删除指定站点，涉及到遍历所有线路和每条线路的站点列表。
  - 更新站点ID时同样需要遍历每个站点。
  - 删除相关的换乘关系时，遍历所有换乘关系。
  - 总体来说，涉及大量的遍历操作，因此时间复杂度为 O(n^2)。

### toggle_station_status

- **时间复杂度**: O(n)
- **分析**:
  - 需要更新指定站点及其相关的直接换乘站点的状态，涉及遍历换乘关系和站点列表。
  - 保存数据和重新绘制线路图都是线性操作，与站点数量成正比。

### add_transfer

- **时间复杂度**: O(n)
- **分析**:
  - 更新站点和换乘关系的操作涉及遍历所有线路和换乘关系。
  - 刷新界面和绘制线路图都是线性操作。

### delete_transfer

- **时间复杂度**: O(n)
- **分析**:
  - 删除指定的换乘关系及其反向关系需要遍历所有换乘关系。
  - 刷新界面和绘制线路图的复杂度也是线性的。

### modify_path

- **时间复杂度**: O(1)
- **分析**:
  - 在指定线路的站点列表中，直接根据索引修改权重，不涉及遍历所有站点。
  - 保存数据和重新绘制线路图也是常数时间操作。

总体来说，这些函数中的大部分操作都是线性的，只有删除站点的操作涉及到了二次方级别的时间复杂度，因为它需要在所有线路和站点中查找和删除指定的站点。

# 4 关键算法测试

## 4.1 同条线路可达

![image-20240704091753727](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704091753727.png)

![image-20240704091800529](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704091800529.png)

![image-20240704091806393](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704091806393.png)

## 4.2 同线路不可达

在以上基础上关闭中春路，测试不可达的情况

![image-20240704092451792](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092451792.png)

## 4.3 不同路线经过换乘可达

![image-20240704092508881](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092508881.png)

![image-20240704092516245](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092516245.png)

## 4.4 不同路线经过换乘可达

### 4.4.1 本身无路线

![image-20240704092607070](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092607070.png)

![image-20240704092612778](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092612778.png)

### 4.4.2 封闭了换乘站

![image-20240704092554407](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092554407.png)

![image-20240704092627369](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092627369.png)

### 4.4.3 封闭了非换乘站



![image-20240704092633341](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092633341.png)

## 4.5 最短路径查找

同一个起始站点，最少换乘和最少时间所选择的路线不同。

![image-20240704092706990](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240704092706990.png)

**最少换乘：**

![image-20240705014203991](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240705014203991.png)

![3919bd72bbaf8a4a409fde31cd44171](C:\Users\Lenovo\Documents\WeChat Files\wxid_b1c8ewn6ic5d22\FileStorage\Temp\3919bd72bbaf8a4a409fde31cd44171.png)

**最少换乘：**

![image-20240705014210015](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240705014210015.png)

**核心转乘递归函数**

```python
if current == end:
    current_transfers = 0
    previous_line = -1
    for i in range(len(path) - 1):
        current_station = path[i]
        next_station = path[i + 1]
        current_line = next((line['lineName'] for line in data['lines'] if
                             any(s['stationName'] == current_station for s in line['stations']) and
                             any(s['stationName'] == next_station for s in line['stations'])), None)

        if previous_line == -1:
            previous_line = current_line
        elif previous_line != current_line:
            current_transfers += 1
            previous_line = current_line

    if current_transfers < least_transfers:
        best_path = path[:]
        least_transfers = current_transfers

```



# 5 总结

本项目为地铁线路管理系统提供了一个综合性的解决方案，通过一个图形用户界面（GUI）使得地铁站点和换乘关系的管理变得直观和易操作。系统支持多种功能，如添加或删除站点、查看和管理换乘关系、修改站点间的权重（代表时间或距离）.。

核心算法采取了图的数据结构与多种查询方式，有效将所学知识应用到具体的项目中，极大地提高了小组成员对算法的理解度与积极性。
