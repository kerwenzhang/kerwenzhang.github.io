---                
layout: post            
title: "Angular单元测试"                
date:   2022-10-25 14:30:00                 
categories: "Web"                
catalog: true                
tags:                 
    - Web                
---      


Angular 框架为我们提供了三大工具，帮助我们更愉快地编写和运行单元测试：  

`Jasmine`：一款主流的测试框架。  
`Karma`：一款主流的单元测试执行引擎。  
`Angular testing utilities`：一个工具类，增强在 Angular 框架下，编写单元测试的体验。  
在使用 Angular CLI 创建项目的同时，单元测试环境也已经配置好了，可以直接编写单元测试。运行命令 `ng test` 运行所有测试。  

Anglar CLI 会自动生成 Jasmine 和 Karma 的配置文件。  
`Karma` 的配置文件是 `karma.conf.js`，可以配置各种插件，测试文件的位置，测试覆盖测量工具，报表形式，以及指定不同的浏览器运行测试。  

Angular 测试工具类帮助我们创建编写单元测试的环境，主要包括 `TestBed` 类和各种助手方法，都位于 @angular/core/testing 名称空间下。  
`TestBed` 类是一个很重要的概念，他会创建一个测试模块，模拟一个正常的 Angular 模块的行为。我们可以通过 `configureTestingModule` 方法配置这个测试模块。  

测试文件的扩展名必须是 `.spec.ts`，这样工具才能识别出它是一个测试文件，也叫规约（spec）文件。  

# 创建测试工程

创建一个新的Angular工程  

    ng new UnittestDemo

运行单元测试： 

    ng test

在命令行中会有如下输出:  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/unittest1.png?raw=true)
Chrome会被调起：  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/unittest2.png?raw=true)

## 调式单元测试代码
如果测试没能如预期般工作，可以在浏览器中查看和调试它们。在浏览器中调试这些测试规约的方式与调试应用时相同。  
打开 Karma 的浏览器窗口，单击 `DEBUG` 按钮；它会打开一个新的浏览器选项卡并重新运行测试。  
打开浏览器的 “Developer Tools”（Ctrl-Shift-I 或 F12）选择 “sources” 页。  
Ctrl+P, 打开 app.component.spec.ts 测试文件  
在测试中设置一个断点。  
刷新浏览器，它会在这个断点处停下来。  

## Coverage

要生成覆盖率报告，请在项目的根目录下运行以下命令。  

    ng test --no-watch --code-coverage

测试完成后，该命令会在项目中创建一个 /coverage 目录。打开 index.html 文件，可以查看带有源代码和代码覆盖率值的报表。  
![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/unittest3.png?raw=true)
如果要在每次测试时都创建代码覆盖率报告，可以在 CLI 配置文件 angular.json 中设置以下选项：  

    "test": {
        "options": {
            "codeCoverage": true
        }
    }

在算覆盖率的时候如果想排除掉某些文件：  

    "test": {
        "options": {
            "codeCoverageExclude": [
                "src/assets/**"
            ]
        }
    }

# Jasmine
Angular 使用了Jasmine测试框架，打开app.component.spec.ts  

    describe('AppComponent', () => {
        beforeEach(async () => {
            await TestBed.configureTestingModule({
            declarations: [
                AppComponent
            ],
            }).compileComponents();
        });

        it('should create the app', () => {
            const fixture = TestBed.createComponent(AppComponent);
            const app = fixture.componentInstance;
            expect(app).toBeTruthy();
        });

        it(`should have as title 'UnitTestDemo'`, () => {
            const fixture = TestBed.createComponent(AppComponent);
            const app = fixture.componentInstance;
            expect(app.title).toEqual('UnitTestDemo');
        });

        it('should render title', () => {
            const fixture = TestBed.createComponent(AppComponent);
            fixture.detectChanges();
            const compiled = fixture.nativeElement as HTMLElement;
            expect(compiled.querySelector('.content span')?.textContent).toContain('UnitTestDemo app is running!');
        });
    });


describe 用于对测试进行分组，通常每个测试文件在顶层都有一个。字符串参数`'AppComponent'`用于命名测试集合。这有助于在大型套件中查找测试。  
`it` 单元测试函数，就像 describe 一样，它需要一个字符串和一个函数。字符串是标题，函数是具体的测试。一个单元测试包含一个或多个`expect`。   
`expect`是对或错的断言。它接受一个值，称为实际值，与预期值进行比较。  

## beforeEach
`beforeEach`、`afterEach`、`beforeAll` 和 `afterAll` 函数  
顾名思义，beforeEach 函数在每个单元测试执行之前被调用一次， 调用 beforeEach() 来为每一个 it() 测试设置前置条件  
在每个测试之后调用一次 afterEach 函数。  
在 describe 中的所有测试运行之前， beforeAll 函数仅被调用一次  
并且在所有规范完成后调用 afterAll 函数  

# Angular TestBed
`TestBed` 是 Angular 测试实用工具中最重要的。TestBed 创建了一个动态构造的 Angular 测试模块，用来模拟一个 Angular 的 @NgModule。  
`TestBed.configureTestingModule()` 方法接受一个元数据对象，它可以拥有@NgModule的大部分属性。  
要测试某个服务，你可以在元数据属性 providers 中设置一个要测试或模拟的服务数组。  

    let service: ValueService;

    beforeEach(() => {
        TestBed.configureTestingModule({ providers: [ValueService] });
    });

将服务类作为参数调用 TestBed.inject()，将它注入到测试中。  

    beforeEach(() => {
        TestBed.configureTestingModule({ providers: [ValueService] });
        service = TestBed.inject(ValueService);
    });



# 测试一个服务

# 测试一个组件
组件不仅仅是它的类。组件还会与 DOM 以及其他组件进行交互。只对类的测试可以告诉你类的行为。但它们无法告诉你这个组件是否能正确渲染、响应用户输入和手势，或是集成到它的父组件和子组件中。  

## ComponentFixture
ComponentFixture 是一个测试挽具，用于与所创建的组件及其对应的元素进行交互。  
可以通过测试夹具（fixture）访问组件实例，并用 Jasmine 的期望断言来确认它是否存在.  


    describe('BannerComponent (with beforeEach)', () => {
        let component: BannerComponent;
        let fixture: ComponentFixture<BannerComponent>;

        beforeEach(() => {
            TestBed.configureTestingModule({declarations: [BannerComponent]});
            fixture = TestBed.createComponent(BannerComponent);
            component = fixture.componentInstance;
        });

        it('should create', () => {
            expect(component).toBeDefined();
        });
        it('should contain "banner works!"', () => {
                const bannerElement: HTMLElement = fixture.nativeElement;
                expect(bannerElement.textContent).toContain('banner works!');
            });
    });

## 组件绑定
createComponent() 不绑定数据   
在生产环境中，当 Angular 创建一个组件，或者用户输入按键，或者异步活动（比如 AJAX）完成时，就会自动进行变更检测。 该 TestBed.createComponent 不会触发变化检测  
必须通过调用 fixture.detectChanges() 来告诉 TestBed 执行数据绑定。只有这样，`<h1>` 才能拥有预期的标题。  

    let component: BannerComponent;
    let fixture: ComponentFixture<BannerComponent>;
    let h1: HTMLElement;

    beforeEach(() => {
        TestBed.configureTestingModule({
            declarations: [ BannerComponent ],
        });
        fixture = TestBed.createComponent(BannerComponent);
        component = fixture.componentInstance; // BannerComponent test instance
        h1 = fixture.nativeElement.querySelector('h1');
    });
    it('should display original title after detectChanges()', () => {
        fixture.detectChanges();
        expect(h1.textContent).toContain(component.title);
    });

### 自动变更检测
可以通过配置带有 ComponentFixtureAutoDetect 提供者的 TestBed 来让 Angular 测试环境自动运行变更检测。  

    import { ComponentFixtureAutoDetect } from '@angular/core/testing';
    TestBed.configureTestingModule({
        declarations: [ BannerComponent ],
        providers: [
            { provide: ComponentFixtureAutoDetect, useValue: true }
        ]
    });

ComponentFixtureAutoDetect 服务会响应异步活动，比如 Promise、定时器和 DOM 事件。但却看不见对组件属性的直接同步更新。该测试必须用 fixture.detectChanges() 来触发另一个变更检测周期。  

    it('should display original title', () => {
        // Hooray! No `fixture.detectChanges()` needed
        expect(h1.textContent).toContain(comp.title);
    });

    it('should still see original title after comp.title change', () => {
        const oldTitle = comp.title;
        comp.title = 'Test Title';
        // Displayed title is old because Angular didn't hear the change :(
        expect(h1.textContent).toContain(oldTitle);
    });

    it('should display updated title after detectChanges', () => {
        comp.title = 'Test Title';
        fixture.detectChanges(); // detect changes explicitly
        expect(h1.textContent).toContain(comp.title);
    });

## 具有依赖的组件
组件通常都有服务依赖。  

    import { Component, OnInit } from '@angular/core';
    import { UserService } from '../model/user.service';

    @Component({
        selector: 'app-welcome',
        template: '<h3 class="welcome"><i>{{welcome}}</i></h3>'
    })
    export class WelcomeComponent implements OnInit {
        welcome = '';
        constructor(private userService: UserService) { }

        ngOnInit(): void {
            this.welcome = this.userService.isLoggedIn ?
            'Welcome, ' + this.userService.user.name : 'Please log in.';
        }
    }

待测组件不必注入真正的服务。事实上，如果它们是测试替身（stubs，fakes，spies 或 mocks），通常会更好。该测试规约的目的是测试组件，而不是服务，使用真正的服务可能会遇到麻烦。  

    let userServiceStub: Partial<UserService>;

    beforeEach(() => {
        // stub UserService for test purposes
        userServiceStub = {
            isLoggedIn: true,
            user: { name: 'Test User' },
        };

        TestBed.configureTestingModule({
            declarations: [ WelcomeComponent ],
            providers: [ { provide: UserService, useValue: userServiceStub } ],
        });

        fixture = TestBed.createComponent(WelcomeComponent);
        comp    = fixture.componentInstance;

        // UserService from the root injector
        userService = TestBed.inject(UserService);

        //  get the "welcome" element by CSS selector (e.g., by class name)
        el = fixture.nativeElement.querySelector('.welcome');
    });

    it('should welcome "Bubba"', () => {
        userService.user.name = 'Bubba'; // welcome message hasn't been shown yet
        fixture.detectChanges();
        expect(el.textContent).toContain('Bubba');
    });

## 带异步服务的组件

[https://angular.cn/guide/testing-components-scenarios#component-with-async-service](https://angular.cn/guide/testing-components-scenarios#component-with-async-service)

# 测试管道
可以在没有 Angular 测试工具的情况下测试管道。  
title-case.pipe.ts:  

    import { Pipe, PipeTransform } from '@angular/core';

    @Pipe({name: 'titlecase', pure: true})
    /** Transform to Title Case: uppercase the first letter of the words in a string. */
    export class TitleCasePipe implements PipeTransform {
        transform(input: string): string {
            return input.length === 0 ? '' :
            input.replace(/\w\S*/g, (txt => txt[0].toUpperCase() + txt.slice(1).toLowerCase() ));
        }
    }

title-case.pipe.spec.ts:  

    describe('TitleCasePipe', () => {
        // This pipe is a pure, stateless function so no need for BeforeEach
        const pipe = new TitleCasePipe();

        it('transforms "abc" to "Abc"', () => {
            expect(pipe.transform('abc')).toBe('Abc');
        });

        it('transforms "abc def" to "Abc Def"', () => {
            expect(pipe.transform('abc def')).toBe('Abc Def');
        });

        // ... more tests ...
    });



# Reference 
[Angular测试](https://angular.cn/guide/testing)  
[Jasmine](https://jasmine.github.io/tutorials/your_first_suite)  
[Angular 单元测试简介](https://www.jianshu.com/p/ab84653ce166)  
[聊聊Angular中的单元测试](https://www.muzhuangnet.com/show/48871.html)  