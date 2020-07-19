# 后端API文档



[TOC]

## 课程

### 查询所有课程

说明：获取所有课程的全部信息

请求方法：GET

请求地址：`/<version>/courses`

请求参数：无

成功条件：总是成功

成功返回：

`状态码200`

| 字段    | 说明     | 类型  | 备注 |
| ------- | -------- | ----- | ---- |
| courses | 课程列表 | Array |      |

- courses的每一项为

| 字段       | 说明             | 类型   | 备注     |
| ---------- | ---------------- | ------ | -------- |
| cid        | 课程id           | Number | 不会缺省 |
| name_zh    | 课程中文名       | String | 不会缺省 |
| name_en    | 课程英文名       | String | 不会缺省 |
| intro      | 课程简介         | String |          |
| pre_Course | 预修课程         | String |          |
| textbooks  | 课本             | String |          |
| semester   | 开课学期         | String |          |
| enroll     | 课程注册人员列表 | Array  |          |

- enroll的每一项为

| 字段        | 说明               | 类型   | 备注                         |
| ----------- | ------------------ | ------ | ---------------------------- |
| user_gid    | 注册该课程的用户id | Number |                              |
| course_id   | 课程id             | Number |                              |
| enroll_type | 用户种类           | Number | 学生0，助教2，老师3，管理员4 |

### 创建课程

说明：创建新课程。需要token，仅管理员能操作

请求方法：POST

请求地址：`/<version>/courses`

成功条件：请求参数符合要求，token和身份验证符合要求

请求参数：

| 字段         | 说明         | 类型              | 备注            | 是否必填 |
| ------------ | ------------ | ----------------- | --------------- | -------- |
| name_zh      | 课程中文名   | String            |                 | 是       |
| name_en      | 课程英文名   | String            |                 | 是       |
| intro        | 课程简介     | String            |                 | 是       |
| pre_Course   | 预修课程信息 | String            |                 | 是       |
| textbooks    | 课本信息     | String            |                 | 是       |
| semester     | 开课学期信息 | String            |                 | 是       |
| teachers_gid | 教师gid列表  | String组成的Array | 缺省默认值'gid' | 是       |
| students_gid | 学生gid列表  | String组成的Array | 缺省默认值'gid' | 是       |
| TAs_gid      | 助教gid列表  | String组成的Array | 缺省默认值'gid' | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | String | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

### 查询单个课程

说明：根据课程id查询单个课程信息；需要token，仅老师和管理员能请求

请求方法：POST

请求地址：`/<version>/courses/<int:cid>`

成功条件：课程存在，token和身份验证成功

请求参数：无

成功返回：

`状态码200`

| 字段       | 说明             | 类型   | 备注     |
| ---------- | ---------------- | ------ | -------- |
| cid        | 课程id           | Number | 不会缺省 |
| name_zh    | 课程中文名       | String | 不会缺省 |
| name_en    | 课程英文名       | String | 不会缺省 |
| intro      | 课程简介         | String |          |
| pre_Course | 预修课程         | String |          |
| textbooks  | 课本             | String |          |
| semester   | 开课学期         | String |          |
| enroll     | 课程注册人员列表 | Array  |          |

- enroll的每一项为

| 字段        | 说明               | 类型   | 备注                         |
| ----------- | ------------------ | ------ | ---------------------------- |
| user_gid    | 注册该课程的用户id | Number |                              |
| course_id   | 课程id             | Number |                              |
| enroll_type | 用户种类           | Number | 学生0，助教2，老师3，管理员4 |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改课程内容

说明：根据课程id修改课程内容，仅老师和管理员能操作

请求方法：PUT

请求地址：`/<version>/courses/<int:cid>`

成功条件：表单参数合法，token验证通过，身份验证通过，课程存在

请求参数：

| 字段             | 说明                    | 类型              | 备注            | 是否必填 |
| ---------------- | ----------------------- | ----------------- | --------------- | -------- |
| name_zh          | 课程中文名              | String            | 缺省时不做改动  | 否       |
| name_en          | 课程英文名              | String            | 缺省时不做改动  | 否       |
| intro            | 课程简介                | String            | 缺省时不做改动  | 否       |
| pre_Course       | 预修课程信息            | String            | 缺省时不做改动  | 否       |
| textbooks        | 课本信息                | String            | 缺省时不做改动  | 否       |
| semester         | 开课学期信息            | String            | 缺省时不做改动  | 否       |
| new_teachers_gid | 新增的教师gid列表       | String组成的Array | 缺省默认值'gid' | 是       |
| new_students_gid | 新增的学生gid列表       | String组成的Array | 缺省默认值'gid' | 是       |
| TAs_gid          | 新增的助教gid列表       | String组成的Array | 缺省默认值'gid' | 是       |
| del_teachers_gid | 需要删除的教师gid列表   | String组成的Array | 缺省默认值'gid' | 是       |
| new_students_gid | 需要删除的的学生gid列表 | String组成的Array | 缺省默认值'gid' | 是       |
| del_TAs_gid      | 需要删除的助教gid列表   | String组成的Array | 缺省默认值'gid' | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

- 请求参数不符合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

### 删除课程

说明：根据课程id删除存在的课程，需要token，仅管理员能操作

请求方法：DELETE

请求地址：`/<version>/courses/<int:cid>`

成功条件：课程存在，token和身份验证通过

请求参数：无

成功返回：

`状态码202`

| 字段       | 说明     | 类型   | 值   |
| ---------- | -------- | ------ | ---- |
| request    | String   |        |      |
| msg        | 返回信息 | String | 'ok' |
| error_code | 错误码   | Number | 1    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 获得课程资源

说明：根据课程id获得课程资源信息

请求方法：GET

请求地址：`/<version>/courses/<int:cid>/files`

成功条件：课程存在

请求参数：无

成功返回：

`状态码200`

| 字段  | 说明             | 类型  | 备注 |
| ----- | ---------------- | ----- | ---- |
| files | 课程资源信息列表 | Array |      |

- files的每一项为

| 字段 | 说明     | 类型   | 备注 |
| ---- | -------- | ------ | ---- |
| id   | 资源id   | Number |      |
| name | 资源名称 | String |      |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 获取课程所有问题

说明：根据课程id获取课程所有问题

请求方法：GET

请求地址：`/<version>/courses/<int:cid>/questions`

成功条件：课程存在

成功返回：

一个Array。每项为

| 字段    | 说明                 | 类型   | 备注 |
| ------- | -------------------- | ------ | ---- |
| id      | 课程资源信息列表     | Number |      |
| title   | 问题标题             | String |      |
| tags    | 该问题所属的所有标签 | Array  |      |
| content | 问题内容             | String |      |

- 其中，tags的每项为

| 字段 | 说明   | 类型   | 备注 |
| ---- | ------ | ------ | ---- |
| id   | 标签id | Number |      |
| name | 标签名 | String |      |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

## 教学日程

日程安排以周为单位。每个课程在每周都能有一个或多个日程安排。每个日程安排由若干个作业组成。

### 为课程创建日程

说明：根据课程id创建为课程**创建某一周的日程安排**，需token，仅老师和管理员能使用

请求方法：POST

请求地址：`/<version>/courses/<int:cid>/schedules`

成功条件：课程存在，token和身份验证通过，请求参数合法

请求参数：

| 字段      | 说明             | 类型   | 备注 | 是否必填 |
| --------- | ---------------- | ------ | ---- | -------- |
| week_id   | 该日程所在的周数 | Number |      | 是       |
| topic     | 主题             | String |      | 是       |
| reference | 参考             | String |      | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 获某课程的日程安排

说明：根据课程id获取课程所有日程安排

请求方法：GET

请求地址：`/<version>/courses//<int:cid>/schedules`

成功条件：课程存在

请求参数：无

成功返回：

`状态码200`

一个列表，列表中的每项为

| 字段        | 说明                   | 类型   | 备注 |
| ----------- | ---------------------- | ------ | ---- |
| id          | Number                 | Number |      |
| course_id   | 该日程安排所在周数     | Numer  |      |
| topic       | 该日程安排的主题       | String |      |
| reference   | 参考                   | String |      |
| assignments | 该日程的作业信息的列表 | Array  |      |

- 其中，assignments的每项为

| 字段        | 说明               | 类型   | 备注      |
| ----------- | ------------------ | ------ | --------- |
| id          | 作业id             | Number |           |
| schedule_id | 该作业所在的日程id | Number |           |
| title       | 作业内容           | String |           |
| due         | 作业截止时间       | Number | timestamp |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 查询某个日程安排

说明：根据日程安排的id查询某个日程安排

请求方法：GET

请求地址：`/<version>/schedules/<int:sid>`

成功条件：该日程存在

成功返回：

`状态码200`

| 字段               | 说明                   | 类型   | 备注 |
| ------------------ | ---------------------- | ------ | ---- |
| id                 | Number                 |        |      |
| 该日程安排所在周数 | Numer                  |        |      |
| topic              | 该日程安排的主题       | String |      |
| reference          | 参考                   | String |      |
| assignments        | 该日程的作业信息的列表 | Array  |      |

- 其中，assignments的每项为

| 字段        | 说明               | 类型   | 备注      |
| ----------- | ------------------ | ------ | --------- |
| id          | 作业id             | Number |           |
| schedule_id | 该作业所在的日程id | Number |           |
| title       | 作业内容           | String |           |
| due         | 作业截止时间       | Number | timestamp |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改日程安排

说明：根据日程id修改已经存在的日程安排，需要token，仅助教，老师，管理员能操作

请求方法：POST

请求地址：`/<version>/schedules/<int:sid>`

成功条件：日程存在，token和身份验证成功

请求参数：

| 字段      | 说明             | 类型   | 备注 | 是否必填 |
| --------- | ---------------- | ------ | ---- | -------- |
| week_id   | 该日程所在的周数 | Number |      | 是       |
| topic     | 主题             | String |      | 是       |
| reference | 参考             | String |      | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 日程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

- 请求参数不符合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

## 作业

### 为日程创建作业

说明：根据日程安排id为日程安排创建作业，需要token，仅助教，老师，管理员能操作

请求方法：POST

请求地址：`/<version>/schedules/<int:sid>/assignments`

成功条件：日程安排存在，token验证通过，身份验证通过，请求参数合法

请求参数：

| 字段  | 说明             | 类型   | 备注      | 是否必填 |
| ----- | ---------------- | ------ | --------- | -------- |
| title | 该日程所在的周数 | String |           | 是       |
| due   | 作业截止时间     | Number | timestamp | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 日程安排不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 查询作业信息

说明：根据作业(assignment)的id查询作业信息

请求方法：GET

请求地址：`/<version>/assignments/<int:aid>`

成功条件：作业存在

请求参数：无

成功返回：

`状态码200`

| 字段        | 说明               | 类型   | 备注      |
| ----------- | ------------------ | ------ | --------- |
| id          | 作业id             | Number |           |
| schedule_id | 该作业所在的日程id | Number |           |
| title       | 作业内容           | String |           |
| due         | 作业截止时间       | Number | timestamp |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改作业信息

说明：根据作业id修改作业信息，需token，仅助教，老师，管理员能操作

请求方法：POST

请求地址：`/<version>/assignments/<int:aid>`

成功条件：作业存在，请求参数合法，token和身份验证成功

请求参数：

| 字段  | 说明             | 类型   | 备注      | 是否必填 |
| ----- | ---------------- | ------ | --------- | -------- |
| title | 该日程所在的周数 | String |           | 是       |
| due   | 作业截止时间     | Number | timestamp | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 作业不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

- 请求参数不符合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

## 课程资源

### 创建课程资源

说明：创建新的课程资源。新创建的资源中无文件，需另上传。需token，仅助教，老师，管理员能操作。

请求方法：POST

请求地址：`/<version>/resources`

成功条件：请求参数合法，请求参数中的course_id对应的课程存在

请求参数：

| 字段      | 说明   | 类型   | 备注         | 是否必填 |
| --------- | ------ | ------ | ------------ | -------- |
| title     | 资源名 | String |              | 是       |
| course_id | 课程id | String | 课程必须存在 | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 权限验证失败时：

`状态码403`

| 字段       | 说明     | 类型   | 值                        |
| ---------- | -------- | ------ | ------------------------- |
| request    | 请求内容 | String |                           |
| msg        | 返回信息 | String | 'forbidden, not in scope' |
| error_code | 错误码   | Number | 1004                      |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 上传资源

说明：为已经创建的资源上传文件

请求方法：PUT

请求地址：`/<version>/resources/<int:fid>`

成功条件：资源存在

请求参数：以name='file'上传文件

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注              |
| ---------- | -------- | ------ | ----------------- |
| request    | 请求内容 | String |                   |
| msg        | 返回信息 |        | Invalid parameter |
| error_code | 错误码   | Number | 1000              |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 下载资源

说明：根据资源id下载文件

请求方法：GET

请求地址：`/<version>/resources/<int:fid>`

成功条件：资源存在

请求参数：无

成功返回：

以附件形式返回文件。Headers中的Content-Disposition中的filename为资源名称。文件在Body中。

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

## 问题

### 为课程创建问题

说明：根据课程id为课程创建问题，需要token

请求方法：POST

请求地址：`/<version>/courses/<int:cid>/questions`

成功条件：token验证通过，课程存在，请求参数合法

请求参数：

| 字段    | 说明             | 类型              | 备注                   | 是否必填 |
| ------- | ---------------- | ----------------- | ---------------------- | -------- |
| week_id | 该日程所在的周数 | Number            |                        | 是       |
| content | 问题内容         | String            |                        | 是       |
| tags    | 问题标签列表     | String组成的Array | 不存在时自动创建新标签 | 否       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改问题

说明：根据问题id修改问题，需要token

请求方法：PUT

请求地址：`/<version>/questions/<int:qid>`

成功条件：token验证通过，课程存在，请求参数合法

请求参数：

| 字段     | 说明                 | 类型              | 备注                   | 是否必填 |
| -------- | -------------------- | ----------------- | ---------------------- | -------- |
| title    | 问题标题             | String            |                        | 否       |
| content  | 问题内容             | String            |                        | 否       |
| new_tags | 新增问题标签列表     | String组成的Array | 不存在时自动创建新标签 | 否       |
| del_tags | 要删除的问题标签列表 | String组成的Array |                        | 否       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 课程不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 删除问题

说明：根据问题id删除问题，需要token

请求方法：DELETE

请求地址：`/<version>/questions/<int:qid>`

成功条件：token验证成功，问题存在

成功返回：

`状态码202`

| 字段       | 说明     | 类型   | 值   |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | 'ok' |
| error_code | 错误码   | Number | 1    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 问题不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 查询问题信息

说明：根据问题id获得问题信息

请求方法：GET

请求地址：`/<version>/questions/<int:qid>`

成功条件：问题存在

成功返回：

`状态码200`

| 字段    | 说明         | 类型   | 备注 |
| ------- | ------------ | ------ | ---- |
| id      | 问题id       | Number |      |
| title   | 问题标题     | String |      |
| tags    | 问题标签列表 | Array  |      |
| content | 问题内容     | String |      |

- 其中，tags的每一项为

| 字段 | 说明   | 类型   | 备注 |
| ---- | ------ | ------ | ---- |
| id   | 标签id | Number |      |
| name | 标签名 | Number |      |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 查询问题历史记录

说明：根据问题id获得问题信息

请求方法：GET

请求地址：`/<version>/questions/<int:qid>/history`

成功条件：问题存在

成功返回：

`状态码200`

一个列表，每项为

| 字段    | 说明          | 类型   | 备注 |
| ------- | ------------- | ------ | ---- |
| id      | 问题id        | Number |      |
| title   | 问题标题      | String |      |
| tags    | 创建/修改时间 |        |      |
| content | 问题内容      | String |      |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 投票/取消

说明：未投票时该请求进行投票，已投票时该请求取消投票

请求方法：POST

请求地址：`<version>/questions/<int:qid>/like`

成功条件：问题存在

请求参数：无

成功返回：

- 成功投票时：

`状态码201`

| 字段       | 说明     | 类型   | 值                     |
| ---------- | -------- | ------ | ---------------------- |
| request    | String   |        |                        |
| msg        | 返回信息 | String | 'up vote successfully' |
| error_code | 错误码   | Number | 0                      |

- 成功取消时：

`状态码201`

| 字段       | 说明     | 类型   | 值                  |
| ---------- | -------- | ------ | ------------------- |
| request    | String   |        |                     |
| msg        | 返回信息 | String | 'up vote cancelled' |
| error_code | 错误码   | Number | 0                   |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| 请求内容   |          |        |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 请求票数

说明：请求一个问题的得票数

请求方法：GET

请求地址：`/<version>/questions/<int:qid>/like`

成功条件：问题存在

成功返回：

`状态码200`

| 字段  | 说明 | 类型   | 备注 |
| ----- | ---- | ------ | ---- |
| likes | 票数 | Number |      |

失败返回：

`状态码404`

| 字段       | 说明         | 类型   | 值                   |
| ---------- | ------------ | ------ | -------------------- |
| request    | 本次请求信息 | String |                      |
| msg        | 返回信息     | String | 'resource not found' |
| error_code | 错误码       | Number | 1001                 |

## 答案

### 为问题创建答案

说明：根据问题id为该问题创建答案，需要token

请求方法：POST

请求地址：`/<version>/questions/<int:qid>/answers`

成功条件：问题存在

请求参数：

| 字段    | 说明     | 类型   | 备注 | 是否必填 |
| ------- | -------- | ------ | ---- | -------- |
| content | 答案内容 | String |      | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 问题不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 查询某个问题的答案

说明：根据问题的id查询答案信息

请求方法：GET

请求地址：`/<version>/questions/<int:qid>/answers`

成功条件：问题存在

请求参数：无

成功返回：

`状态码200`

一个列表，列表的每项为

| 字段    | 说明     | 类型   | 是否必填         |
| ------- | -------- | ------ | ---------------- |
| id      | aid      | Number | 不会缺省         |
| content | 答案内容 | String | 不会缺省         |
| stars   | star数   | Number | 不存在时返回null |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改答案内容

说明：修改已有回答的内容

请求方法：PUT

请求地址：`/<version>/answers/<int:aid>/update`

成功条件：答案存在，请求参数符合要求

请求参数：

| 字段    | 说明     | 类型     | 默认值 | 是否必填 |
| ------- | -------- | -------- | ------ | -------- |
| content | 回答内容 | textarea |        | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 状态码   | number |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- 答案不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 状态码   | Number |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

- 请求参数不符合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

### 查询单个答案

说明：请求已有答案的信息

请求方法：GET

请求地址：`/<version>/answers/<int:aid>`

请求参数：无

成功条件：答案存在

成功返回：

`状态码200`

| 字段    | 说明     | 类型   | 是否必填         |
| ------- | -------- | ------ | ---------------- |
| id      | aid      | Number | 不会缺省         |
| content | 答案内容 | String | 不会缺省         |
| stars   | star数   | Number | 不存在时返回null |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 状态码   | Number |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 删除答案

说明：删除已经存在的答案

请求方法：DELETE

请求地址：`<version>/answers/<int:aid>`

请求参数：无

成功条件：答案存在

成功返回：

`状态码202`

| 字段       | 说明     | 类型   | 值   |
| ---------- | -------- | ------ | ---- |
| request    | 状态码   | String |      |
| msg        | 返回信息 | String | 'ok' |
| error_code | 错误码   | Number | 1    |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 状态码   | Number |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 投票/取消

说明：未投票时该请求进行投票，已投票时该请求取消投票

请求方法：POST

请求地址：`<version>/answers/<int:aid>/like`

成功条件：答案存在

成功返回：

- 成功投票时：

`状态码201`

| 字段       | 说明     | 类型   | 值                     |
| ---------- | -------- | ------ | ---------------------- |
| request    | 状态码   | String |                        |
| msg        | 返回信息 | String | 'up vote successfully' |
| error_code | 错误码   | Number | 0                      |

- 成功取消时：

`状态码201`

| 字段       | 说明     | 类型   | 值                  |
| ---------- | -------- | ------ | ------------------- |
| request    | 状态码   | String |                     |
| msg        | 返回信息 | String | 'up vote cancelled' |
| error_code | 错误码   | Number | 0                   |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| code       | 请求内容 | Number |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 请求票数

说明：请求一个答案的得票数

请求方法：GET

请求地址：`answers/<int:aid>/like`

成功条件：答案存在

成功返回：

`状态码200`

| 字段  | 说明 | 类型   | 备注 |
| ----- | ---- | ------ | ---- |
| likes | 票数 | Number |      |

失败返回：

`状态码404`

| 字段       | 说明         | 类型   | 值                   |
| ---------- | ------------ | ------ | -------------------- |
| request    | 本次请求信息 | String |                      |
| msg        | 返回信息     | String | 'resource not found' |
| error_code | 错误码       | Number | 1001                 |

## 讨论

### 创建讨论主题

说明：根据问题id为该问题创建一个讨论主题，需要token

请求方法：POST

请求地址：`/<version>/questions/<int:qid>/discussions`

成功条件：问题存在，token验证通过，请求参数合法

请求参数：

| 字段    | 说明         | 类型   | 备注 | 是否必填 |
| ------- | ------------ | ------ | ---- | -------- |
| title   | 讨论主题标题 | String |      | 是       |
| content | 讨论主题内容 | String |      | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 问题不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

### 查询问题的讨论主题

说明：根据问题id获得问题的讨论主题

请求方法：GET

请求地址：`/<version>/questions/<int:qid>/discussions`

成功条件：问题存在

成功返回：

`状态码200`

一个列表，每项为

| 字段       | 说明         | 类型   | 备注 |
| ---------- | ------------ | ------ | ---- |
| id         | 讨论主题id   | Number |      |
| title      | 讨论主题标题 | String |      |
| stars      | star数       | Number |      |
| title      | 讨论标题     | String |      |
| content    | 讨论主题内容 | String |      |
| author_gid | 作者gid      | String |      |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改讨论主题

说明：根据讨论主题id修改讨论主题，需要token

请求方法：PUT

请求地址：`/<version>/discussions/<int:did>`

成功条件：token验证通过，讨论主题存在，请求参数合法

请求参数：

| 字段    | 说明         | 类型   | 备注 | 是否必填 |
| ------- | ------------ | ------ | ---- | -------- |
| title   | 讨论主题标题 | String |      | 否       |
| content | 讨论主题内容 | String |      | 否       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 讨论主题不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 删除讨论主题

说明：根据讨论主题id删除主题，需要token

请求方法：DELETE

请求地址：`/<version>/discussions/<int:did>`

成功条件：token验证成功，讨论主题存在

成功返回：

`状态码202`

| 字段       | 说明     | 类型   | 值   |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | 'ok' |
| error_code | 错误码   | Number | 1    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 讨论主题不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 为一个讨论主题添加讨论回帖

说明：根据讨论主题id为该问题添加一个回帖，需要token

请求方法：POST

请求地址：`/<version>/discussions/<int:did>/answer`

成功条件：讨论主题存在，请求参数合法

请求参数：

| 字段    | 说明     | 类型   | 备注 | 是否必填 |
| ------- | -------- | ------ | ---- | -------- |
| title   |          | String |      | 否       |
| content | 回帖内容 | String |      | 是       |

成功返回：

`状态码201`

| 字段       | 说明     | 类型   | 备注 |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | ‘ok' |
| error_code | 错误码   | Number | 0    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 讨论主题不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

### 查询一个讨论主题的所有回帖

说明：根据讨论主题id获得主题的所有回帖

请求方法：GET

请求地址：`/<version>/discussions/<int:did>/answer`

成功条件：主题存在

成功返回：

`状态码200`

一个列表，每项为

| 字段       | 说明       | 类型   | 备注 |
| ---------- | ---------- | ------ | ---- |
| id         | 回帖id     | Number |      |
| title      | 讨论主题id | Number |      |
| content    | 回帖内容   | String |      |
| author_gid | 作者gid    | String |      |
| reply_id   |            | Number |      |

失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 获取单个回帖信息

说明：根据回帖id获得回帖信息

请求方法：GET

请求地址：`/<version>/topic_answers/<int:topic_answer_id>`

成功条件：回帖存在

成功返回：

`状态码200`

| 字段       | 说明       | 类型   | 备注 |
| ---------- | ---------- | ------ | ---- |
| id         | 回帖id     | Number |      |
| title      | 讨论主题id | Number |      |
| content    | 回帖内容   | String |      |
| author_gid | 作者gid    | String |      |
| reply_id   |            | Number |      |

- 失败返回：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 修改回帖

说明：根据回帖id修改回帖，需要token

请求方法：PUT

请求地址：`/<version>/topic_answers/<int:topic_answer_id>`

成功条件：token验证通过，回帖存在，请求参数合法

请求参数：

| 字段     | 说明     | 类型   | 备注 | 是否必填 |
| -------- | -------- | ------ | ---- | -------- |
| reply_id |          | Number |      | 否       |
| content  | 回帖内容 | String |      | 是       |

成功返回：修改后的回帖信息

`状态码201`

| 字段       | 说明       | 类型   | 备注 |
| ---------- | ---------- | ------ | ---- |
| id         | 回帖id     | Number |      |
| title      | 讨论主题id | Number |      |
| content    | 回帖内容   | String |      |
| author_gid | 作者gid    | String |      |
| reply_id   |            | Number |      |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 备注                                                         |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 参数不合要求时：

`状态码400`

| 字段       | 说明     | 类型   | 备注                   |
| ---------- | -------- | ------ | ---------------------- |
| request    | 请求内容 | String |                        |
| msg        | 返回信息 | Object | 说明哪些请求参数不合法 |
| error_code | 错误码   | Number | 1004                   |

- 要修改的回帖不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |

### 删除回帖

说明：根据回帖id删除回帖，需要token

请求方法：DELETE

请求地址：`/<version>/topic_answers/<int:topic_answer_id>`

成功条件：token验证成功，回帖存在

成功返回：

`状态码202`

| 字段       | 说明     | 类型   | 值   |
| ---------- | -------- | ------ | ---- |
| request    | 请求内容 | String |      |
| msg        | 返回信息 | String | 'ok' |
| error_code | 错误码   | Number | 1    |

失败返回：

- token验证失败时：

`状态码401`

| 字段       | 说明     | 类型   | 值                                                           |
| ---------- | -------- | ------ | ------------------------------------------------------------ |
| request    | 请求内容 | String |                                                              |
| msg        | 返回信息 | String | token过期为`Token expired`; token无效为`Token invalid`;token缺失为`Token missing` |
| error_code | 错误码   | Number | token过期为1003，token无效为1002，token缺失为1004            |

- 回帖不存在时：

`状态码404`

| 字段       | 说明     | 类型   | 值                   |
| ---------- | -------- | ------ | -------------------- |
| request    | 请求内容 | String |                      |
| msg        | 返回信息 | String | 'resource not found' |
| error_code | 错误码   | Number | 1001                 |