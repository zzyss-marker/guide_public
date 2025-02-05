pip install -r requirements.txt

mysql-connector-python与数据库连接

数据库 (Database)：存储数据的容器，类似Excel文件。

表 (Table)：数据库中结构化数据的集合，类似Excel的工作表。

字段 (Column)：表的列，表示数据的属性（如“姓名”、“年龄”）。

记录 (Row)：表中的一行数据。

show databases;
show tables;
show columns from table;（describe table;）

1. **用户表（users）**
   - 用户 ID（主键）
   - 用户名
   - 密码
   - 用户角色（学生/教师/管理员）

2. **场地预约表（venue_reservations）**
   - 预约 ID（主键）
   - 用户 ID（外键，指向用户表）
   - 场地类型（讲座/研讨室/会议室）
   - 预约日期
   - 商务时间段（下午/晚上）
   - 用途
   - 设备需求（大屏、笔记本、话筒等）
   - 设备绑定信息（如果选择了笔记本，投屏器也要绑定）

3. **设备借用表（device_reservations）**
   - 设备借用 ID（主键）
   - 用户 ID（外键）
   - 设备类型（电动螺丝刀、万用表等）
   - 借用时间
   - 预计归还时间
   - 借用原因

4. **3D 打印机预约表（3d_printer_reservations）**
   - 打印机预约 ID（主键）
   - 用户 ID（外键）
   - 打印机类型（打印机1、2、3）
   - 预约日期
   - 打印时间

5. **设备和场地管理表（admin管理）**
   - 设备/场地 ID（主键）
   - 设备/场地名称
   - 库存数量
   - 设备类型
   - 状态（可用/已借用等）
