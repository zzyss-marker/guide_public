程序挂载 nohup python your_program.py &

htop查程序pid    杀进程 kill \<PID\>

Ctrl+z	将当前程序放到后台运行，恢复到前台为命令fg

# 前后端tips
在前后端开发中，前端和后端各自有不同的职责，通常通过HTTP请求和响应来进行数据交换。具体流程可以大致分为以下几个步骤：

### 1. 前端的角色与作用
前端负责用户界面的展示和交互，通常用HTML、CSS和JavaScript来构建。具体到你正在做的小程序，Vue是一个JavaScript框架，主要用于构建用户界面，提供更高效、更便捷的开发方式。

- **Vue的作用**：Vue 是一个渐进式框架，帮助你更方便地管理前端的数据和界面，尤其是处理用户交互、数据绑定和视图更新。它通过“组件化”的方式，将页面拆分成不同的功能模块，每个模块都有自己的逻辑和界面，从而提高代码的可维护性和复用性。
  
- **Vue的工作原理**：Vue 的核心是数据驱动视图。当数据变化时，Vue 会自动更新页面上的相关部分，而无需你手动操作DOM。这是通过双向绑定和虚拟DOM技术实现的。

### 2. 后端的角色与作用
后端负责处理前端发送的请求，处理数据逻辑，存储和管理数据，并返回给前端。后端常使用Python、Java、Node.js等语言来开发。

- **Django的作用**：Django 是一个基于Python的Web框架，能够帮助你快速构建后端应用，提供了很多功能如数据库操作、认证、路由等。通过 Django，后端可以定义API（接口）来接收前端的请求，处理数据，并返回响应。

- **后端的工作原理**：当用户在前端页面上提交表单或进行其他操作时，前端会通过HTTP请求（如GET、POST等）将数据发送到后端。后端收到请求后，进行数据处理（例如从数据库获取数据、进行计算或执行其他操作），然后返回一个响应给前端。

### 3. 前后端如何交互？
前后端交互通常依靠HTTP协议（或WebSocket等协议）来进行。具体来说，前端发起请求，后端接收请求并返回结果。

- **前端发送请求**：在Vue中，你可以使用JavaScript的`fetch`或`axios`库来向后端发起请求。例如：

```javascript
// 使用axios向后端发送请求
import axios from 'axios';

axios.post('http://your-api-url.com/data', { key: 'value' })
  .then(response => {
    console.log('响应数据:', response.data);
  })
  .catch(error => {
    console.error('请求错误:', error);
  });
```

- **后端处理请求**：后端的Django会接收到前端的请求，然后通过相应的视图函数处理请求。例如，Django的视图可以是一个接收POST请求的函数，它会处理请求并返回一个JSON响应。

```python
from django.http import JsonResponse

def your_view(request):
    if request.method == 'POST':
        data = request.POST
        # 处理数据
        response_data = {'message': '成功'}
        return JsonResponse(response_data)
```

### 4. 前端如何修改后端数据？
通常前端通过向后端发送POST请求来修改后端的数据。例如，前端发送一个表单数据到后端，后端接收到数据后修改数据库中的相应记录。这个过程完全由前端的JavaScript控制，例如你在Vue中的方法，来触发这种操作。

### 5. 总结
- **Vue**：是前端框架，负责展示和交互逻辑。你用它来构建用户界面，并与后端交互。
- **Django**：是后端框架，处理前端请求，进行数据处理，并返回响应。
- **交互**：前端通过JavaScript的`axios`或`fetch`向后端发送请求，后端处理请求后返回数据，前端再根据数据更新界面。

通过这样的流程，前后端可以高效协作，形成完整的Web应用或小程序。在你的项目中，前端通过Vue来管理UI，后端通过Django处理逻辑和数据库交互，两者通过API连接。



Vue框架与HTML、CSS、JavaScript的关系，以及JavaScript是否是后端语言，可以从以下几个方面解答：

---

### **1. Vue 与 HTML、CSS 的关系**

#### **HTML（结构层）**
HTML 是网页的结构语言，用来定义网页的内容和布局。Vue 是基于 HTML 工作的，它的模板语法（Template）实际上就是扩展了 HTML。

- **Vue 如何使用 HTML**：在 Vue 中，你仍然需要写 HTML 标签来定义页面结构，但可以通过 Vue 提供的模板语法（如`v-bind`、`v-for`、`v-if`）动态渲染内容。例如：

```html
<div id="app">
  <p v-if="isVisible">这是动态显示的内容。</p>
</div>
```

上面的代码中，`v-if="isVisible"`是 Vue 扩展的语法，它根据`isVisible`变量动态决定内容是否显示。

#### **CSS（表现层）**
CSS 是网页的样式语言，用来定义 HTML 元素的外观。Vue 并不取代 CSS，而是让你可以在组件中更加方便地管理样式。

- **Vue 如何使用 CSS**：Vue 支持将 CSS 和 HTML 组合在一起，使每个组件的样式独立。例如：

```html
<template>
  <div class="box">Hello Vue!</div>
</template>

<style scoped>
.box {
  color: blue;
  font-size: 20px;
}
</style>
```

通过`scoped`，你可以将样式限制在当前组件内部，避免影响全局样式。

#### **总结**
Vue 是一个框架，它本质上是对 HTML 和 CSS 的增强，使开发者可以更高效地构建动态界面。它不会替代 HTML 和 CSS，而是基于它们进行工作。

---

### **2. JavaScript 是后端语言吗？**

JavaScript 不是严格意义上的后端语言，而是一种**“前后端通用”的编程语言**。它最早是为前端开发设计的，但后来也可以用于后端开发。

#### **前端中的 JavaScript**
JavaScript 最初的用途是让网页具有交互性，比如：
- 表单验证
- 动态修改页面内容
- 与用户进行交互（如点击按钮时弹出提示）

在 Vue 中，JavaScript 是核心语言，负责数据处理、事件监听和与后端的通信。例如：

```javascript
export default {
  data() {
    return {
      message: 'Hello Vue!'
    };
  },
  methods: {
    changeMessage() {
      this.message = 'Vue is awesome!';
    }
  }
};
```

#### **后端中的 JavaScript**
随着 Node.js 的出现，JavaScript 也可以用来构建后端应用。Node.js 是一个基于 JavaScript 的运行时环境，允许 JavaScript 运行在服务器端。通过 Node.js，开发者可以使用 JavaScript 来处理后端逻辑，例如：
- 操作数据库
- 编写 API
- 处理文件系统

例如，一个简单的 Node.js 服务器：

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello from the server!');
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

#### **总结**
- JavaScript 在前端用于动态交互，在 Vue 中是核心语言。
- JavaScript 在后端可以通过 Node.js 实现后端功能。
- 它不是传统的后端语言，但已经成为一种“全栈语言”。

---

### **3. Vue、HTML、CSS 和 JavaScript 的整体关系**
- **HTML**：提供页面结构。
- **CSS**：提供页面样式。
- **JavaScript**：提供页面的动态行为。
- **Vue**：基于 HTML、CSS 和 JavaScript，为开发者提供了一个高效的工具，帮助你更轻松地管理界面、数据和逻辑。

如果把网页比作一栋房子：
- HTML 是房子的框架；
- CSS 是房子的装修；
- JavaScript 是房子里的电路、开关等，让房子“动起来”；
- Vue 是一个施工工具包，帮助你快速建造房子、管理房子的功能。
