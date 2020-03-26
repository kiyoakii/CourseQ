## 前端开发工具

前端开发工具有很多，轻量型的编辑器如 VSCode，Atom， Sublime 等，IDE型的工具如 HBuilder，WebStorm 等。经过讨论，我们决定选用 VSCode 来进行前端开发的任务。理由如下：

1. VSCode 可以通过安装相关插件来支持 Vue 开发。
2. VSCode 可以便捷查看 Git Diff 的部分，并选择是否保留远程更新的代码，防止自己的代码进度丢失。
3. VSCode 相较于 IDE 型的工具，更加轻量级，在低配置电脑上也能流畅运行。



## 前端技术选型

### 前端框架选型

现在前端框架常见的有：[Bootstrap](https://github.com/twbs/bootstrap) 和 [JQuery](https://github.com/jquery/jquery)，[Vue.js](https://github.com/vuejs/vue)，[React](https://github.com/facebook/react)，[Angular](https://github.com/angular/angular)。其中，Vue，React，Angular 这三个框架在目前都是已经比较成熟的框架。

框架对比如下：

1. Bootstarp 和 JQuery 是一种快速建站的框架，通过 JQuery 来操作 DOM，通过 Bootstrap 来实现可相应式用户界面，这在以往的 Web 开发中相当常见。但是，随着 Web 应用越来越复杂，将 Web 开发模块化，组件化已经是大势所趋，因此，Bootstrap 和 JQuery 来开发 Web 应用已经越来越不常见了。
2. Vue 是⼀个轻量级的框架，通过进⾏双向数据的绑定来驱动界⾯，很多程序员学习新框架的时候，都会先从Vue开始，因为它的官⽅⽂档介绍的⾮常清楚，⽽且能够⾮常快速的通过异步批处理的方式更新DOM，可以把解耦的、可复⽤的组件组合在⼀起使⽤，还可以允许多种模块的安装，使⽤的场景很灵活。Vue 是⽤于构建交互式的 Web 界⾯的库。它提供了 MVVM 数据绑定和⼀个可组合的组件系统，具有简单、灵活的 API。从技术上讲， Vue.js 集中在 MVVM 模式上的视图模型层，并通过双向数据绑定连接视图和模型。实际的 DOM 操作和输出格式被抽象出来成指令和过滤器。相⽐其它的 MVVM 框架，Vue.js 更容易上⼿，并且也是⽬前市场上⽐较流⾏的前后端分离的开发模式，⼤多前端都是 vue 做的。
3.  React 起源于 Facebook 的内部项⽬，⽤来架设 Instagram 的⽹站， 并于 2013年5 ⽉开源。React 拥有较⾼的性能，代码逻辑⾮常简单，越来越多的⼈已开始关注和使⽤它。React 框架可以通过对DOM的模拟减少与 DOM 的交互，从⽽轻易的解决了跨浏览器兼容的问题，它的模块化把组件隔离，出现问题时⽅便程序员修改，还因为同构JavaScript所以有助于搜索引擎的优化。
4. Angular 是⼀个以 JavaScript 编写的库，是⼀款优秀的前端 JS 框架，已经被⽤于 Google 的多款产品当中。拥有良好的应⽤程序，模板的功能⾮常强⼤，⾃带丰富的 Angular 指令，可以通过指令拓宽 HTML，⽽且可以通过表达式绑定数据到 HTML，因为引⼊了 Java 的⼀些内容，所以很容易就可以写出复⽤代码，有效提⾼了团队开发的速度。Angular 有着诸多特性，最为核⼼的是：MVVM、模块化、⾃动化双向数据绑定、语义化标签、依赖注⼊等等。它的出现⽐较早，也是曾经⽐较流⾏的前端 JS 框架，但是随着 React 与 Vue 的出现，它的热度在慢慢降低。

契合度分析：

从技术上分析，Vue 与 React 都是⽬前市场上⽐较流⾏的前端框架，并且都有丰富的⽂档以及众多开发⼈员维护，版本也很稳定，但是 React 并不是⼀个完整的框架，在开发时基本都需要加上 ReactRouter 和 Flux 才能写⼤型应⽤。Vue 是⼀个轻量级的框架，⽂档详细，简单易上⼿，双向数据绑定、组件复⽤、Vuex 状态管理前后端分离等特性能很好地满⾜项⽬开发的需要。Angular ⽂档例⼦较少，虽然⼊⻔容易，但后期技术掌握起来较难，加之项⽬开发周期有时间限制，因此短时间内熟练使⽤不易实现。至于 Bootstrap 和 JQuery，由于不支持 Web 应用组件化开发，这在开发的时候难以维护，因此不予考虑。

从开发团队成员⾃身分析，近期课程培训前端框架主讲的是 Vue，成员也使⽤ Vue 框架进⾏了作业练习，对 Vue 的双向数据绑定、组件等特性的使⽤已经具备⼀定的基础，能够基于 Vue 框架进⾏前端开发。

综上所述，我们决定选⽤ Vue 框架作为前端开发框架。

### Web 端样式库选型

常见的 Web 端样式库有：[Ant Design](https://github.com/ant-design/ant-design)，[ElementUI](https://github.com/Recklesslmz/elementUI)，[iView](https://github.com/iview/iview) 和 [SUI](https://github.com/sdc-alibaba/SUI-Mobile)。

样式库对比如下：

1.  Ant Design 是⼀个服务于企业级产品的设计体系，基于『确定』和『⾃然』的设计价值观和模块化的解决⽅案，让设计者专注于更好的⽤户体验。
2.  ElementUI 是⼀套为开发者、设计师和产品经理准备的基于 Vue 2.0 的桌⾯端组件，可以方便实现相关的 UI 效果。
3.  iView 是⼀套基于 Vue.js 的开源 UI 组件库，主要服务于 PC 界⾯的中后台产品。
4.  SUI 是⼀套基于 Bootstrap 开发的前端组件库，同时她也是⼀套设计规范。通过 SUI，可以⾮常⽅便的设计和实现精美的⻚⾯。

契合度分析：

首先，我们开发的是 Web 端前台应用，iView 不在我们的选择中。其次 SUI 的关键点在于方便迅速搭建手机 H5 应用，我们的项目主要用于 PC 端，因此，SUI 不在我们的选择中。Ant Design 和 ElementUI 中，我们发现 ElementUI 更契合我们的项目，同时相较于 Ant Design，ElementUI 更容易上手，因此，我们最终选择 ElementUI 作为我们的样式库。

### 前端包管理工具选型

前端包管理工具主要有 [yarn](https://github.com/yarnpkg/yarn) 和 [npm](https://github.com/npm/cli)。

包管理工具对比如下：

1. yarn 的速度快，yarn执行安装时是并行安装，同时支持离线模式，减少网络负载。其次，安装版本统一，为了防止拉取到不同的版本，yarn 会在项目根目录下面创建一个锁定文件记录被确切安装上的模块的版本号。同时，yarn 具有更加简洁的输出和更好的语义化。
2. npm 是默认的前端管理工具，在 npm 5.0 之后，也做了一些改进，但是在速度上还是没有超过 yarn。

契合度分析：

从需求上讲，npm 和 yarn 都能提供很好的包管理的功能，同时，从对比中可以看出，yarn 的安装依赖的速度更快，因此我们选择 yarn 作为我们的包管理工具。

### 前端 Markdown 编辑器选型

[Maven Editor](https://github.com/hinesboy/mavonEditor) 是一个成熟的基于 Vue 的 Markdown 编辑器，界面美观，功能强大。它的主要优势包括：

1. 支持粗体、斜体、标题、下划线、中划线、标记、上角标、下角标、引用、有序列表、无序列表、链接、图片链接、代码块、表格。并且自带了其他额外的功能，诸如上一步、下一步、清空、保存、导航目录、左对齐、居中、右对齐、单双栏模式、实时预览等。
2. 界面简洁美观，不熟悉 Markdown 语法的用户也可以使用工具栏的按钮来快捷生成 Markdown 语法，极大降低了用户的学习成本和使用门槛。
3. 可以与语法高亮插件 [Highlight.js](https://github.com/highlightjs/highlight.js) 配合使用，提升代码展示的美观性，对计算机相关学科的学生十分友好。
4. 可以与专为 Web 软件定制的快速数学公式渲染插件 [KaTex](https://github.com/KaTeX/KaTeX) 配合使用，满足用户插入公式的需求。
5. 该插件文档详尽，易于理解，且为开发者提供了丰富的自定义选项，对开发者十分友好。

综上所述，Maven Editor 完美契合了我们的需求，我们选择这个插件作为前端 Markdown 编辑器。





