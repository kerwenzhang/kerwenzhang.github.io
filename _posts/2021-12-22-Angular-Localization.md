---                
layout: post            
title: "Angular本地化"                
date:   2021-12-22 17:30:00                 
categories: "web"                
catalog: true                
tags:                 
    - web                
---      

Angular本地化有两种方式，一种是Angular官网推荐的`i18n`标记，另外一种是`ngx-translate`  

# Angular
## Angular/localize
要利用 Angular 的本地化功能，请用 Angular CLI 将 @angular/localize 包添加到你的项目中。  

    ng add @angular/localize

Angular 提供了以下内置的数据转换管道。数据转换管道会使用 LOCALE_ID 标记来根据每个语言环境的规则来格式化数据。  

    DatePipe ：格式化日期值。
    CurrencyPipe ：将数字转换为货币字符串。
    DecimalPipe ：将数字转换为十进制数字字符串。
    PercentPipe ：将数字转换为百分比字符串。

## 添加 i18n 标记
标记要翻译的文本  
使用 `i18n` 属性标记要翻译的组件模板中的静态文本消息。将它放在每个元素标签上，并带有要翻译的固定文本。  
例如，以下 `<h1>` 标记显示简单的英语问候语 `Hello World！`。  

    <h1>Hello World!</h1>

要将问候语标记为待翻译，请将 `i18n` 属性添加到 `<h1>` 标记。  

    <h1 i18n>Hello World!</h1>

## 提取源语言文件
要提取源语言文件，请打开终端窗口，切换到应用程序项目的根目录，然后运行以下 CLI 命令：  

    ng extract-i18n

`extract-i18n` 命令使用 `XML` 在项目的根目录中创建一个名为 `messages.xlf` 的源语言文件。  
要在 `src/locale` 目录中创建文件，请在选项中指定输出路径。以下示例就在选项中指定了输出路径。  

    ng extract-i18n --output-path src/locale

要创建法语翻译文件，请执行以下步骤：  
1. 制作 `messages.xlf` 源语言文件的副本。  
2. 将副本放在 `src/locale` 文件夹中。  
3. 将副本重命名为 `messages.fr.xlf` 以进行法语 ( fr ) 翻译。将此翻译文件发送给翻译人员。  

Angular需要为每个语言环境构建应用程序的可分发文件的副本。  
合并翻译后，可使用“服务器的语言检测功能”或不同的子目录来提供应用程序的每个可分发副本。  

# ngx-translate
Angular官网的方式需要构建不同的语言版本，并且没法自由切换语言。  
另一种方式是用开源库 `ngx-translate`。  
创建一个新的Angular工程 `ng new local`  
安装`ng-translate`：  

    npm install @ngx-translate/core@13.0.0 --save
    npm install @ngx-translate/http-loader --save

在`assets`文件夹下创建 国际化语言文件夹 `i18n`，在`i18n`文件夹下创建相应的语言包文件  
en.json:  

    {
        "welcome":"Welcom",
        "descripition":"This is description"
    }

zh.json:  

    {
        "welcome":"欢迎",
        "descripition":"这是描述信息"
    }

在根模块`app.module.ts` 导入该模块  

    import {TranslateModule, TranslateLoader} from '@ngx-translate/core';
    import {TranslateHttpLoader} from '@ngx-translate/http-loader';
    import {HttpClient, HttpClientModule} from '@angular/common/http';

    // AoT requires an exported function for factories
    export function HttpLoaderFactory(httpClient: HttpClient) {
    return new TranslateHttpLoader(httpClient);
    }

    @NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        TranslateModule.forRoot({
        loader: {
            provide: TranslateLoader,
            useFactory: HttpLoaderFactory,
            deps: [HttpClient]
        }
        })
    ],
    providers: [],
    bootstrap: [AppComponent]
    })
    export class AppModule { }

注意要在import里添加`HttpClientModule`的引用。  
app.component.html  

    <div>
        <h2>{{ 'HOME.TITLE' | translate }}</h2>
        <label>
            {{ 'HOME.SELECT' | translate }}
            <select #langSelect (change)="translate.use(langSelect.value)">
                <option *ngFor="let lang of translate.getLangs()" [value]="lang" [selected]="lang === translate.currentLang">{{ lang }}</option>
            </select>
        </label>
    </div>

app.component.ts  

    export class AppComponent {
        constructor(public translate: TranslateService) {
            translate.addLangs(['en', 'zh']);
            translate.setDefaultLang('en');

            const browserLang = translate.getBrowserLang();
            translate.use(browserLang.match(/en|zh/) ? browserLang : 'en');
        }
    }


## 在懒加载module里使用
### ForChild

如果采用了angular的子模块懒加载功能的话，则需要对子模块也进行配置, 导入的文件包和函数配置等都是相同的，只有imports注入的时候不太一样，需要使用`forChild()`的方法  
`ng g m modules/module1 --routing` 生成子模块module1  
module1.module.ts  

    import { HttpClient, HttpClientModule } from '@angular/common/http';
    import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
    import { TranslateHttpLoader } from '@ngx-translate/http-loader';

    // AoT requires an exported function for factories
    export function HttpLoaderFactory(httpClient: HttpClient) {
        return new TranslateHttpLoader(httpClient);
    }

    @NgModule({
        declarations: [],
        imports: [
            CommonModule,
            HttpClientModule,
            TranslateModule.forChild({
                loader: {
                    provide: TranslateLoader,
                    useFactory: HttpLoaderFactory,
                    deps: [HttpClient]
                }
            })
        ]
    })

ng g c modules/module1/module1生成component  
module1.component.html:  

    <div>
        <h2>{{ 'HOME.TITLE' | translate }}</h2>    
    </div>

module1-routing.module.ts:  

    const routes: Routes = [
        {
            path:'',
            component:Module1Component
        }
    ];

app-routing.module.ts  

    const routes: Routes = [
        { 
            path:'', 
            redirectTo: 'module1', 
            pathMatch: 'full' 
        },
        {
            path:'module1',
            loadChildren: ()=> import('./modules/module1/module1.module').then(m => m.Module1Module)
        }
    ];

app.component.html:  

    <router-outlet></router-outlet>
    <div>
        <label>
            {{ 'HOME.SELECT' | translate }}
            <select #langSelect (change)="translate.use(langSelect.value)">
                <option *ngFor="let lang of translate.getLangs()" [value]="lang" [selected]="lang === translate.currentLang">{{ lang }}</option>
            </select>
        </label>
    </div>

### Pipe
也可以用Pipe的方式，将Pipe封装成一个module，在其他懒加载的module里引用。  



# 比较

ngx-translate的开发者 Olivier Combe 对这两种方式做了比较，原文：  

The idea behind this lib has always been to provide support for i18n until Angular catches up, after that this lib will probably be deprecated. For now, there are still a few differences between Angular i18n and this library:  

1. Angular only works with one language at a time, you have to completely reload the application to change the lang. The JIT support only means that it works with JIT, but you still have to provide the translations at bootstrap because it will replace the text in your templates during the compilation whereas this lib uses bindings, which means that you can change the translations at any time. The downside is that bindings take memory, so the Angular way is more performant. But if you use OnPush for your components you will probably never notice the difference  
2. Angular only supports using i18n in your templates for now, I'm working on the feature that will allow you to use it in your code, but it's still a work in progress. This lib works both in code and templates  
3. Angular supports either XLIFF or XMB (both are XML formats), whereas this lib supports JSON by default but you can write your own loader to support any format that you want (there's a loader for PO files for example)  
4. Angular supports ICU expressions (plurals and select), but this library doesn't  
5. Angular supports html placeholders including angular code, whereas this library only supports regular html (because it's executed at runtime, and not during compilation, and there is no $compile in Angular like there was in AngularJS)  
6. The API of this library is more complete because it is executed at runtime it can offer more things (observables, events, ...) which Angular doesn't have (but doesn't really need given that you can not change the translations)

[Angular 国际化](https://angular.cn/guide/i18n-overview)  
[angular6.x 国际化解决方案 ngx-translate](https://www.jianshu.com/p/9c3834b9feed)  
[Why ngx-translate exists if we already have built-in Angular2+ i18n](https://github.com/ngx-translate/core/issues/495)