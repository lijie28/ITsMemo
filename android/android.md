## 项目构成

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

Controller(references、UI Data)->viewGroup