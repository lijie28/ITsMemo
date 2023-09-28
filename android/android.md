# 项目构成

### 环境等配置
build.gradle(安卓版本配置，库管理，build settings相当)

AndroidManifest.xml（App信息、权限管理，info.plist相当）

---
### 入口
MainActivity (APP生命周期管理，AppDelegate相当)
>Activity 类提供六个核心回调：onCreate()、onStart()、onResume()、onPause()、onStop() 和 onDestroy()
>https://developer.android.com/guide/components/activities/activity-lifecycle?hl=zh-cn

---
### UI布局
Fragment(碎片UI，必需依附Activity，有单独的生命周期)

><p>onAttach()&#xff1a;Fragment和Activity相关联时调用。可以通过该方法获取Activity引用&#xff0c;还可以通过getArguments()获取参数。</p> 
><p>onCreate()&#xff1a;Fragment被创建时调用。</p> 
><p>onCreateView()&#xff1a;创建Fragment的布局。</p>
><p>onActivityCreated()&#xff1a;当Activity完成onCreate()时调用。</p> 
><p>onStart()&#xff1a;当Fragment可见时调用。</p> 
><p>onResume()&#xff1a;当Fragment可见且可交互时调用。</p> 
><p>onPause()&#xff1a;当Fragment不可交互但可见时调用。</p> 
><p>onStop()&#xff1a;当Fragment不可见时调用。</p> 
><p>onDestroyView()&#xff1a;当Fragment的UI从视图结构中移除时调用。</p> 
><p>onDestroy()&#xff1a;销毁Fragment时调用。</p> 
><p>onDetach()&#xff1a;当Fragment和Activity解除关联时调用。</p> 

---
res/下的xxx.xml (storyboard似的拉线布局，也可通过code直接编辑)

在xml里设置控件id后，可以通过findViewById可以找到对应控件

文字类: strings.xml

---
### 屏幕翻转处理
可以通过 'Create Landscape Variation' 单独设置横屏布局
屏幕翻转中会经过onDestory和onCreate，不加处理的话页面上数据会丢失（可以用Bundle的saveInstanceState和方法onSaveInstanceState处理）

---
### Android Jetpack
官方引导的库, androidx.*

---
### ViewModel
Jetpack下的一个模块，处理页面数据，MVVM里的VM 
- androidx.livecycle.ViewModel

---
### LiveData
数据更新后通知页面更新用
- androidx.livecycle.MutableLiveData
- 与ViewModel绑定 ViewModelProvider.of(activity).get(liveData)
- 需要具体数据设置observe

---
### DataBinding 
ViewModel与View双向绑定用
- 在xml里小灯泡提示convert to data binding layout
- ActivityMianBinding(能直接获取xml里的控件标签为成员)
- 在xml的标签data/variable/type:viewModel后，可在控件处直接@{}代码方式引用（button的onclick也可以引用viewModel里的方法）

---
### 持久保持数据
SharedPreferences (UserDefault相当)

---
### MVC
- M: Model
- V: View(xml+Activity)
- C: Controller(Activity，与View不解耦)

### MVP
- M: Model
- V: View(xml+Activity)
- P: Presenter(从Activity里脱离，单独处理逻辑，与View之间存在Interface)

### MVVM
现主流，Google支持
- M: Model
- V: View(xml)
- VM: ViewModel(通过DataBinding与View双向绑定)

ViewModelScope生命周期比Activity长

### 多线程
通过Thread()里实行run()方法，也可继承Thread重写run
> new Thread() {  
&emsp;public void run() {  
&emsp;&emsp;// ... 耗时操作  
&emsp;&emsp;&emsp;// 回到UI主线程  
&emsp;&emsp;&emsp;runOnUiThread(new Runnable) {  
&emsp;&emsp;&emsp;&emsp;@Override  
&emsp;&emsp;&emsp;&emsp;public void run() {  
&emsp;&emsp;&emsp;&emsp;}  
&emsp;&emsp;&emsp;}  
&emsp;&emsp;}  
}

### Http请求
HttpUrlConnection ,和swift的URLSession/URLRequest用法差不多

OkHttp, 非官方库，但写起来更简洁
> https://square.github.io/okhttp/

# Kotlin
### 语法

变量:
- val (read-only)不可变
- var (mutable)可变

---
### 与swift相似
可在: 后声明类型
> val c: Int

有for in 循环
> for (item in items) { }

和range
> for (x in 1..10) { }

有函数的默认参数
> fun foo(a: Int = 0, b: String = "")

检测元素是否存在于集合中
> if ("john@example.com" in emailsList) { …… }

遍历 map/pair型list
>for ((k, v) in map) {
    println("$k -> $v")
}

类与属性写法基本相似
> class Address {<br>
    var name: String = "Holmes, Sherlock"<br>
    var street: String = "Baker"<br>
    var city: String = "London"<br>
    var state: String? = null<br>
    var zip: String = "123456"<br>
}

---
### 与swift不同
有 When 表达式 （取代switch）
>fun main() {<br>
    val items = setOf("apple", "banana", "kiwifruit")<br>
    when {<br>
        "orange" in items -> println("juicy")<br>
        "apple" in items -> println("apple is fine too")<br>
    }
}

If not null and else 缩写
> kotlin: files?.size ?: "empty"

> swift: files?.size ?? "empty"

单例、用object修饰
> object Resource {
    val name = "Name"
}

interface
> swift的protocol、实现时也不需要加extension修饰

---
### 继承
默认情况下，Kotlin 类是最终（final）的：它们不能被继承。 要使一个类可继承，请用 open 关键字标记它。
> open class Base // 该类开放继承

需要重写的方法成员同样需要open
> open class Shape {  
    open val vertexCount: Int = 0  
    open fun draw() { /*……*/ }  
    fun fill() { /*……*/ }  
}

---
### 扩展
直接 fun 类名.方法 { ... }
> class User(var name:String)  
扩展函数:  
fun User.Print(){  
    print("用户名 $name")  
}

可空接收者
> fun Any?.toString(): String {  
    if (this == null) return "null"  
    // 空检测之后，“this”会自动转换为非空类型，所以下面的 toString()  
    // 解析为 Any 类的成员函数  
    return toString()  
}

能扩展属性
> class Snake{  
    var aaa = 1  
}  
var Snake.size:Int  
    set(value) {aaa = value}  
    get() = aaa +1  

但不能有初始化器
> val House.number = 1 // 错误：扩展属性不能有初始化器

---
### 枚举类
枚举类的最基本的用法是实现类型安全的枚举：
> enum class Direction {  
    NORTH, SOUTH, WEST, EAST  
}

自 Kotlin 1.1 起，可以使用 enumValues<T>() 与 enumValueOf<T>() 函数以泛型的方式访问枚举类中的常量 ：
> enum class RGB { RED, GREEN, BLUE }  
inline fun <reified T : Enum<T>> printAllValues() {  
    print(enumValues<T>().joinToString { it.name })  
}  
printAllValues<RGB>() // 输出 RED, GREEN, BLUE

每个枚举常量都具有在枚举类声明中获取其名称与位置的属性：
> val name: String  
val ordinal: Int

能带参数
> enum class Color(val rgb: Int) {  
        RED(0xFF0000),  
        GREEN(0x00FF00),  
        BLUE(0x0000FF)  
}