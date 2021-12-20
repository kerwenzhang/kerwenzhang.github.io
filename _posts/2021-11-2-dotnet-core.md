---                
layout: post             
title: ".Net core学习笔记"                
date:   2021-11-2 10:30:00                 
categories: ".Net Core"                
catalog: true                
tags:                 
    - .Net Core                
---      

## 基础知识  

### Startup 类  
Startup 类包括：

`ConfigureServices`方法注册应用所需的服务，在 `Configure` 方法配置应用服务之前，由主机调用。  
`Configure`方法创建应用的请求处理管道，中间件   

示例：  

    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<RazorPagesMovieContext>(options =>
                options.UseSqlServer(Configuration.GetConnectionString("RazorPagesMovieContext")));

            services.AddControllersWithViews();
            services.AddRazorPages();
        }

        public void Configure(IApplicationBuilder app)
        {
            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapDefaultControllerRoute();
                endpoints.MapRazorPages();
            });
        }
    }

### 中间件  

请求处理管道由一系列中间件组件组成。 每个组件在 `HttpContext` 上执行操作，调用管道中的下一个中间件或终止请求。  
按照惯例，通过在 Startup.Configure 方法中调用 Use... 扩展方法，向管道添加中间件组件。  

### Host(主机)

ASP.NET Core 应用在启动时构建主机。 主机封装应用的所有资源  

    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                });
    }

### Logging

    public class TodoController : ControllerBase
    {
        private readonly ILogger _logger;

        public TodoController(ILogger<TodoController> logger)
        {
            _logger = logger;
        }

        [HttpGet("{id}", Name = "GetTodo")]
        public ActionResult<TodoItem> GetById(string id)
        {
            _logger.LogInformation(LoggingEvents.GetItem, "Getting item {Id}", id);
            
            // Item lookup code removed.
            
            if (item == null)
            {
                _logger.LogWarning(LoggingEvents.GetItemNotFound, "GetById({Id}) NOT FOUND", id);
                return NotFound();
            }
            
            return item;
        }
    }

### 依赖注入    
ASP.NET Core 支持依赖关系注入 (DI) 软件设计模式  
示例：  
`IMyDependency` 接口定义 `WriteMessage` 方法   

    public interface IMyDependency
    {
        void WriteMessage(string message);
    }

具体类 `MyDependency` 实现此接口  

    public class MyDependency : IMyDependency
    {
        public void WriteMessage(string message)
        {
            Console.WriteLine($"MyDependency.WriteMessage Message: {message}");
        }
    }

在`Startup`中注册服务  

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddScoped<IMyDependency, MyDependency>();
    }

在实际应用中，请求 `IMyDependency` 服务并用于调用 `WriteMessage` 方法：  

    public class IndexModel : PageModel
    {
        private readonly IMyDependency _myDependency;

        public IndexModel(IMyDependency myDependency)
        {
            _myDependency = myDependency;            
        }

        public void OnGet()
        {
            _myDependency.WriteMessage("Index2Model.OnGet");
        }
    }

不使用具体类型 `MyDependency`，仅使用它实现的 `IMyDependency` 接口。 这样可以轻松地更改控制器使用的实现，而无需修改控制器。    


可以将相关的注册组移动到扩展方法以注册服务。  

    using ConfigSample.Options;
    using Microsoft.Extensions.Configuration;

    namespace Microsoft.Extensions.DependencyInjection
    {
        public static class MyConfigServiceCollectionExtensions
        {
            public static IServiceCollection AddConfig(
                this IServiceCollection services, IConfiguration config)
            {
                services.Configure<PositionOptions>(
                    config.GetSection(PositionOptions.Position));
                services.Configure<ColorOptions>(
                    config.GetSection(ColorOptions.Color));

                return services;
            }
        }
    }

下面的 ConfigureServices 方法使用新扩展方法来注册服务   

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddConfig(Configuration)
                .AddMyDependencyGroup();

        services.AddRazorPages();
    }


避免使用服务定位器模式。 例如，可以使用 `DI` 代替时，不要调用 `GetService` 来获取服务实例：    

错误示范：  

    public class MyClass
    {
        public void MyMethod()
        {
            var optionMonitor = _services.GetService<IOptionsMonitor<MyOptions>>();
            var option = optionMonitor.CurrentValue.Option;

            ...
        }
    }
    
正确示范：  

    public class MyClass
    {
        private readonly IOptionsMonitor<MyOptions> _optionsMonitor;

        public MyClass(IOptionsMonitor<MyOptions> optionsMonitor)
        {
            _optionsMonitor = optionsMonitor;
        }

        public void MyMethod()
        {
            var option = _optionsMonitor.CurrentValue.Option;

            ...
        }
    }


## .net
安装https证书

    dotnet dev-certs https --trust


    Dotnet watch run

Add controller  

DataContext

        ervices.AddDbContext<DataContext>(options =>
        {
            options.UseSqlite(_Config.GetConnectionString("DefaultConnection"));
        });

Dotnet-ef

    dotnet ef migrations add InitialCreate -o Data/Migrations

create scheme


## Angular

extension:  
Angular language servcie
Angular snippets
Bracket Pair Colorizer 2


ng add ngx-bootstrap  
npm install font-awesome


app.UseCors(policy => policy.AllowAnyHeader().AllowAnyMethod().WithOrigins("https://localhost:4200"));


https:

        "sslKey": "./ssl/server.key",
        "sslCert": "./ssl/server.cert",
        "ssl": true,
            

## Register/Login

Save hashed password and salt into database


        using var hamc = new HMACSHA512();
        var user = new AppUser
        {
            UserName = username,
            PasswordHash = hamc.ComputeHash(Encoding.UTF8.GetBytes(password)),
            PasswordSalt = hamc.Key
        };
        this.context.Users.Add(user);
        await this.context.SaveChangesAsync();
        return user;


DTOs(Data Transfer Objects)  

parameter validation:
[Required]

dotnet ef database drop  
dotnet ef database update  


JSON Web Tokens(JWT)
header
DATA
    nbf, exp, iat
Signature

![img](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/JWT.png?raw=true)  


Add token service:  
services.AddScoped<ITokenService, TokenService>();

        public string CreateToken(AppUser user)
        {
            var claims = new List<Claim>
            {
                new Claim(JwtRegisteredClaimNames.NameId, user.UserName)
            };

            var creds = new SigningCredentials(_key, SecurityAlgorithms.HmacSha512Signature);
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(claims),
                Expires = DateTime.Now.AddDays(7),
                SigningCredentials = creds
            };
            var tokenHandler = new JwtSecurityTokenHandler();
            var token = tokenHandler.CreateToken(tokenDescriptor);
            return tokenHandler.WriteToken(token);
        }

"TokenKey":"super secret unguessable key",


Add middleware

        services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
                .AddJwtBearer(options =>
                {
                    options.TokenValidationParameters = new TokenValidationParameters
                    {
                        ValidateIssuerSigningKey = true,
                        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_Config["TokenKey"])),
                        ValidateIssuer = false,
                        ValidateAudience = false,
                    };
                });


## Angular login

        <form #loginForm="ngForm" class="form-inline mt-2 mt-md-0" (ngSubmit)="login()" autocomplete="off">
              <input name="username" [(ngModel)]="model.username" class="form-control mr-sm-2" type="text" placeholder="Username">
              <input name="password" [(ngModel)]="model.password" class="form-control mr-sm-2" type="password" placeholder="Password">
              <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Login</button>
        </form>

    

        getMembers() {
            return this.http.get('api/users').pipe(
                map(members => {
                    cosnole.log(member.id);
                    return member.id;
                })
            )
        }

Observables的pipe and map


        private currentUserSource = new ReplaySubject<User>(1);
        currentUser$ = this.currentUserSource.asObservable();


pass parameter to child

Child pass parameter to parent

child:

        @Output() cancelRegister = new EventEmitter();
        this.cancelRegister.emit(false);

Parent:

        <app-register (cancelRegister)="cancelRegisterMode($event)"></app-register>
          cancelRegisterMode(event:boolean):void{
                this.registerMode = event;
            }

npm install ngx-toastr 


Angular route guard:

    ng g guard auth

    canActivate(): Observable<boolean> {
        return this.accountService.currentUser$.pipe(
            map(user => {
                if(user) return true;
                this.toastr.error('You shall not pass!');
                return false;
            })
        )
    }

    {path:'members', component:MemberListComponent, canActivate:[AuthGuard]},


Add a dummy route

    {
        path:'',
        runGuardsAndResolvers:'always',
        canActivate:[AuthGuard],
        children:[
            {path:'members', component:MemberListComponent, canActivate:[AuthGuard]},
            {path:'members/:id', component:MemberDetailComponent},
            {path:'lists', component:ListsComponent},
            {path:'messages', component:MessagesComponent},
        ]
    },

ng-container is normally a better technique for when you're using conditionals. because of the fact it doesn't generate any HTML and it won't interfere with any of your styling when you use it.

    <ng-container *ngIf="accountService.currentUser$ | async">      
        <li class="nav-item">
          <a class="nav-link" routerLink='/members' routerLinkActive='active'>Matches</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" routerLink='/lists' routerLinkActive='active'>Lists</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" routerLink='/messages' routerLinkActive='active'>Messages</a>
        </li>
    </ng-container>

npm install bootswatch

shared module:

    ng g m shared --flat


## Error handling   

        [Required]
        [StringLength(8, MinimumLength = 4)]
        public string Password { get; set; }   

Exception handing middleware

        app.UseMiddleware<ExceptionMiddleware>();

        public async Task InvokeAsync(HttpContext context)
        {
            try
            {
                await this.next(context);
            }
            catch(Exception ex)
            {
                this.logger.LogError(ex, ex.Message);
                context.Response.ContentType = "application/json";
                context.Response.StatusCode = (int) HttpStatusCode.InternalServerError;

                var response = this.Env.IsDevelopment()
                ? new ApiException(context.Response.StatusCode, ex.Message, ex.StackTrace?.ToString())
                : new ApiException(context.Response.StatusCode, "Internal Server Error", "");

                var options = new JsonSerializerOptions();

                var json = JsonSerializer.Serialize(response, options);
                await context.Response.WriteAsync(json);
            }
        }

Error handing in Angular

        ng g interceptor --skip-tests

        providers: [
            {provide: HTTP_INTERCEPTORS, useClass:ErrorInterceptor, multi:true},
        ],


        "lib": [
            "es2019",
        ]



扩展API

        public static class DateTimeExtensions
        {
            public static int CalculateAge(this DateTime dob){
                var today = DateTime.Today;
                var age = today.Year - dob.Year;
                if(dob.Date > today.AddYears(-age)) age--;
                return age;
            }
        }


        public DateTime DateOfBirth { get; set; }
        public int GetAge()
        {
            return DateOfBirth.CalculateAge();
        }

为什么可以直接调用？


        dotnet ef migrations add ExtendedUserEntity
        dotnet ef database update


解析Json 数据


    using System.Text.Json;
    var users = JsonSerializer.Deserialize<List<AppUser>>(userData);


AutoMapperProfiles.cs

        public AutoMapperProfiles()
        {
            CreateMap<AppUser, MemberDto>()
            .ForMember(dest => dest.PhotoUrl, opt => opt.MapFrom(src => 
            src.Photos.FirstOrDefault(x => x.IsMain).Url))
            .ForMember(dest => dest.Age, opt => opt.MapFrom(src => src.DateOfBirth.CalculateAge()));
            CreateMap<Photo, PhotoDto>();
        }


        services.AddAutoMapper(typeof(AutoMapperProfiles).Assembly);

## 问题

1.     dotnet ef migrations add ExtendedUserEntity
        dotnet ef database update


2. 什么是DTO


## Reference

[数字签名是什么](http://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html)  
[什么是数字签名和证书](https://www.jianshu.com/p/9db57e761255)  
[HTTP2和HTTPS来不来了解一下](https://zhuanlan.zhihu.com/p/40902149)  
[Entity Framework Core](https://docs.microsoft.com/zh-cn/ef/core/)  