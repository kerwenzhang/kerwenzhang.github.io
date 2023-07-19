---
layout: post
title: "JavaScript 总结"
date: 2023-07-11 9:00:00
categories: "Web"
catalog: true
tags:
  - Web
---

[HTML](https://blog.csdn.net/wuyxinu/article/details/103515157)  
[CSS](https://blog.csdn.net/wuyxinu/article/details/103583618)  
[JS](https://blog.csdn.net/wuyxinu/article/details/103642800)  
[JS-下](https://blog.csdn.net/wuyxinu/article/details/103646041)  
[jQuery](https://blog.csdn.net/wuyxinu/article/details/103669718)  
[Node.js + Gulp](https://blog.csdn.net/wuyxinu/article/details/103774211)  
[JavaScript 教程](https://wangdoc.com/javascript/)

HTML 是网页的结构，CSS 是网页的外观，而 JavaScript 是页面的行为。

### 历史

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript.jpg?raw=true)

### 变量

变量是对“值”的具名引用。变量就是为“值”起名，然后引用这个名字，就等同于引用这个值。变量的名字就是变量名。

        let a = 1;

#### 变量提升

JavaScript 引擎的工作方式是，先解析代码，获取所有被声明的变量，然后再一行一行地运行。这造成的结果，就是所有的变量的声明语句，都会被提升到代码的头部，这就叫做变量提升（hoisting）。

        console.log(a);
        let a = 1;

等于

        let a;
        console.log(a);
        a = 1;

最后的结果是显示 undefined，表示变量 a 已声明，但还未赋值。

## 数据类型

JavaScript 数据类型有 2 大分类：一是“基本数据类型”，二是“特殊数据类型”。

其中，基本数据类型包括以下 3 种：

（1）数字型（Number 型）：如整型 84，浮点型 3.14；  
（2）字符串型（String 型）：如"绿叶学习网"；  
（3）布尔型（Boolean 型）：true 或 fasle；

特殊数据类型有 3 种：

（1）空值（null 型）；  
（2）未定义值（undefined 型）；  
（3）转义字符；

### 值类型与引用类型

基本数据类型属于值类型，值存储在 Stack 里。 Object 等属于引用类型，存储在 Heap 里  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript2.jpg?raw=true)

当我们申请一个值类型时，我们实际上是在堆栈中申请了一块内存，分配如下：

        let age = 30;

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript3.jpg?raw=true)
当再声明一个变量等于 age 时

        let age = 30;
        let oldAge = age;

在内存中，实际发生的事情是两个变量都指向了同一个内存地址：
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript4.jpg?raw=true)

第三步，当我们修改 age 的值时

        let age = 30;
        let oldAge = age;
        let age = 31;

在内存中，已分配的内存中的值不可再修改（the value at a certain memory address is immutable)，实际发生的事情是变量 age 重新申请了一块新的内存，去存储新的值 31.  
![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript5.jpg?raw=true)

而对于引用类型，当初始化一个引用类型时，变量的值存储在 Heap 里，堆栈的 value 只记录了 heap 的地址。

        const me = {
                age: 30
        }

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript6.jpg?raw=true)  
当定义另一个变量 friend 时, friend 和 me 都指向了同一个内存地址.

        const me = {
                age: 30
        }
        const friend = me;

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript7.jpg?raw=true)  
如果此时修改 friend 的 age， 我们实际上只是修改了 Heap 中存储的 value，Stack 里的地址没有发生任何变化。

        const me = {
                age: 30
        }
        const friend = me;
        friend.age = 27;

![image](https://github.com/kerwenzhang/kerwenzhang.github.io/blob/master/_posts/image/javascript8.jpg?raw=true)
这也解释了一个引用类型声明为 const，我们仍然可以修改它的值

        const testObj = {
                age: 30
        }
        testObj.age = 27;  // allow
        testObj = {}  // not allow, due testObj is const

### Number

JavaScript 内部，所有数字都是以 64 位浮点数形式储存，即使整数也是如此。这就是说，JavaScript 语言的底层根本没有整数，所有数字都是小数（64 位浮点数）。

        1 === 1.0 // true

由于浮点数不是精确的值，所以涉及小数的比较和运算要特别小心。

        0.1 + 0.2 === 0.3        // false
        0.3 / 0.1        // 2.9999999999999996
        (0.3 - 0.2) === (0.2 - 0.1)        // false

### Boolean

5 种 falsy value：

        0, '', undefined, null, NaN

### typeof 运算符

typeof 运算符用于返回它的操作数当前所容纳的数据的类型，这对于判断一个变量是否已被定义特别有用。  
例如：typeof(1)返回值是 number，typeof("javascript")返回值是 string。  
在实际编程中，通常用 tppeof 判断变量是否定义。

        // 错误的写法
        if (v) {
        // ...
        }
        // ReferenceError: v is not defined

        // 正确的写法
        if (typeof v === "undefined") {
        // ...
        }

### NaN

NaN 是 JavaScript 的特殊值，表示“非数字”（Not a Number），主要出现在将字符串解析成数字出错的场合。

isNaN 方法可以用来判断一个值是否为 NaN。

        isNaN(NaN) // true
        isNaN(123) // false

### 对象(object)

对象就是一组“键值对”（key-value）的集合，是一种无序的复合数据集合。

        const jonas = {
                firtName: 'Jonas',
                lastName: 'Schemdtman',
                age: 2023 - 1991,
                job: 'teacher',
                firends: ['Michael', 'Peter', 'Steven']
        };

对象的访问可以使用键值也可以用方括号

        jonas.firstName
        jonas['lastName']

        const nameKey = 'Name';
        jonas['first' + nameKey]        // 可以拼接

检查键值是否存在:

        if(!jonas['location']) {
                console.log('does not exist');
        }

对象的每一个键名又称为“属性”（property），它的“键值”可以是任何数据类型。如果一个属性的值为函数，通常把这个属性称为“方法”，它可以像函数那样调用。

    let obj = {
        p: function (x) {
            return 2 * x;
        }
    };
    obj.p(1) // 2

属性可以动态创建，不必在对象声明时就指定。

        let obj = {};
        obj.foo = 123;
        obj.foo // 123

查看一个对象本身的所有属性，可以使用 Object.keys 方法。

        let obj = {
          key1: 1,
          key2: 2
        };
        Object.keys(obj);
        // ['key1', 'key2']

#### 数组

##### 创建数组

在 JavaScript 中，创建数组共有 3 种方法：

    let myArr = new Array();

    let myArr = new Array(3);
    myArr[0]="HTML";
    myArr[1]="CSS";
    myArr[2]="JavaScript";

    let myArr = new Array(1,2,3,4);     // bad
    let arr = ['a', 'b', 'c'];          // good

本质上，数组属于一种特殊的对象。typeof 运算符会返回数组的类型是 object。

清空数组的一个有效方法，就是将 length 属性设为 0。

        let arr = [ 'a', 'b', 'c' ];
        arr.length = 0;

##### 常用方法

    slice()                  //获取数组中的某段数组元素
    push()                   //在数组末尾添加元素
    pop()                    //删除数组最后一个元素
    toString()               //将数组转换为字符串
    join()                   //将数组元素连接成字符串
    concat()                 //多个数组连接为字符串
    sort()                   //数组元素正向排序
    reverse()                //数组元素反转
    indexOf('subElement')   //返回指定元素的位置
    includes('subElement')  //是否包含指定元素
    shift()                 //移除第一个元素
    unshift('newItem')      //添加新的元素到数组开头

slice()方法的一个重要应用，是将类似数组的对象转为真正的数组。

    Array.prototype.slice.call(document.querySelectorAll("div"));
    Array.prototype.slice.call(arguments);

map()  
map 方法将数组的所有成员依次传入参数函数，然后把每一次的执行结果组成一个新数组返回。

    let numbers = [1, 2, 3];
    numbers.map(function (n) {
        return n + 1;
    });
    // [2, 3, 4]

filter()  
filter 方法用于过滤数组成员，满足条件的成员组成一个新数组返回。

    [1, 2, 3, 4, 5].filter(function (elem) {
        return (elem > 3);
    })
    // [4, 5]

some()，every()  
some 方法是只要一个成员的返回值是 true，则整个 some 方法的返回值就是 true，否则返回 false。

        let arr = [1, 2, 3, 4, 5];
        arr.some(function (elem, index, arr) {
            return elem >= 3;
        });
        // true

every 方法是所有成员的返回值都是 true，整个 every 方法才返回 true，否则返回 false。

unshift()  
将一个或多个元素添加到数组的开头，并返回数组的新长度

        const friends = [ 'Michale', 'Steven', 'Peter'];
        const newLength = friend.unshift('John');
        console.log(friends);     // ['John', 'Michale', 'Steven', 'Peter']
        console.log(newLength);   // 4

#### 字符串对象

1.  字符串模板拼接

        const firstName = Jonas;
        const birthYear = 1991;
        const year = 2037;
        const job = 'teacher'
        const jonas = `I'm ${firstName}, a ${year - bithYear} year old ${job}!`;
        console.log(jonas);

2.  length 属性  
    我们可以通过 length 属性来获取字符串的长度。

            字符串名.length

3.  match()  
    使用 match()方法可以从字符串内索引指定的值，或者找到一个或多个正则表达式的匹配。

            stringObject.match(字符串)    //匹配字符串;
            stringObject.match(正则表达式)  //匹配正则表达式

4.  indexOf()  
    使用 indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置。

            stringObject.indexOf(字符串)

5.  replace()  
    replace()方法常常用于在字符串中用一些字符替换另一些字符，或者替换一个与正则表达式匹配的子串。

            stringObject.replace(原字符,替换字符)
            stringObject.replace(正则表达式,替换字符)  //匹配正则表达式

6.  charAt()  
    使用 charAt()方法来获取字符串中的某一个字符

            stringObject.charAt(n)

7.  连接字符串  
    使用 concat()方法来连接 2 个或多个字符串。

            字符串1.concat(字符串2,字符串3,…,字符串n);

8.  split()  
    使用 split()方法把一个字符串分割成字符串数组。

            字符串.split(分割符)

9.  substring()  
    使用 substring()方法来提取字符串中的某一部分字符串。

            字符串.substring(开始位置,结束位置)

#### 日期对象

创建日期对象必须使用“new 语句”。

    let 日期对象名 = new Date();
    let 日期对象名 = new Date(日期字符串);

常用方法:

    getFullYear()	//返回一个表示年份的4位数字
    getMonth()	//返回值是0（一月）到11（十二月）之间的一个整数
    getDate()	//返回值是1~31之间的一个整数
    getHours()	//返回值是0~23之间的一个整数，来表示小时数
    getMinutes()	//返回值是0~59之间的一个整数，来表示分钟数
    getSeconds()	//返回值是0~59之间的一个整数，来表示秒数

将日期时间转换为字符串:

    toString()	//将日期时间转换为普通字符串
    toUTCString()	//将日期时间转换为世界时间（UTC）格式的字符串
    toLocaleString()	//将日期时间转换为本地时间格式的字符串
    toJSON()            //方法返回一个符合 JSON 格式的 ISO 日期字符串

#### console 对象

1.  `console.warn()`，`console.error()`  
    warn 方法和 error 方法也是在控制台输出信息，它们与 log 方法的不同之处在于，warn 方法输出信息时，在最前面加一个黄色三角，表示警告；error 方法输出信息时，在最前面加一个红色的叉，表示出错。
2.  console.table()  
    对于某些复合类型的数据，console.table 方法可以将其转为表格显示。

        let languages = [
                { name: "JavaScript", fileExtension: ".js" },
                { name: "TypeScript", fileExtension: ".ts" },
                { name: "CoffeeScript", fileExtension: ".coffee" }
        ];
        console.table(languages);

3.  console.count()  
    count 方法用于计数，输出它被调用了多少次。

4.  console.time()，console.timeEnd()  
    这两个方法用于计时，可以算出一个操作所花费的准确时间。

        console.time('Array initialize');
        let array= new Array(1000000);
        for (let i = array.length - 1; i >= 0; i--) {
        array[i] = new Object();
        };
        console.timeEnd('Array initialize');
        // Array initialize: 1914.481ms

5.  console.trace()  
    console.trace 方法显示当前执行的代码在堆栈中的调用路径。

#### RegExp 对象

新建正则表达式有两种方法。一种是使用字面量，以斜杠表示开始和结束。

    let regex = /xyz/;

另一种是使用 RegExp 构造函数。

    let regex = new RegExp('xyz');

第一种方法在引擎编译代码时，就会新建正则表达式，第二种方法在运行时新建正则表达式，所以前者的效率较高。而且，前者比较便利和直观

常用方法：

1.  test()  
    正则实例对象的 test 方法返回一个布尔值，表示当前模式是否能匹配参数字符串。

            /cat/.test('cats and dogs') // true

2.  exec()  
    用来返回匹配结果。如果发现匹配，就返回一个数组，成员是匹配成功的子字符串，否则返回 null。

            let s = '_x_x';
            let r1 = /x/;
            r1.exec(s) // ["x"]

3.  String.match()  
    字符串实例对象的 match 方法对字符串进行正则匹配，返回匹配结果。

            let s = '_x_x';
            let r1 = /x/;
            s.match(r1) // ["x"]

##### 匹配规则

[https://wangdoc.com/javascript/stdlib/regexp.html](https://wangdoc.com/javascript/stdlib/regexp.html)

#### Math 对象

    max(x,y)	//返回x和y中的最大值
    min(x,y)	//返回x和y中的最小值
    pow(x,y)	//返回x的y次幂
    abs(x)	//返回数的绝对值
    random()	//返回0~1之间的随机数
    trunc()     //截取整数部分，舍弃小数部分
    round(x)	//把数四舍五入为最接近的整数
    ceil(x)	//对一个数进行上舍入
    floor(x)	//对一个数进行下舍入

生成一个 1-20 的随机数

        Math.trunc(Math.random() * 20) + 1;

#### JSON 对象

JSON 格式（JavaScript Object Notation 的缩写）是一种用于数据交换的文本格式，2001 年由 Douglas Crockford 提出，目的是取代繁琐笨重的 XML 格式。  
字符串必须使用双引号表示，不能使用单引号。  
对象的键名必须放在双引号里面。  
数组或对象最后一个成员的后面，不能加逗号。

以下都是合法的 JSON。

        ["one", "two", "three"]
        { "one": 1, "two": 2, "three": 3 }
        { name: "张三", "age": 32 }
        {"names": ["张三", "李四"] }
        [ { "name": "张三"}, {"name": "李四"} ]

JSON.stringify()  
将一个值转为 JSON 字符串。该字符串符合 JSON 格式，并且可以被 JSON.parse 方法还原。

        JSON.stringify([1, "false", false])  // '[1,"false",false]'
        JSON.stringify({ name: "张三" })   // '{"name":"张三"}'

JSON.parse()  
JSON.parse 方法用于将 JSON 字符串转换成对应的值。

        let o = JSON.parse('{"name": "张三"}');
        o.name // 张三

### 类型转换

1.  字符串型转换为数值型

        const inputYear = '1991'
        Number(inputYear);
        Number('test string')  // NAN

        String(23);

        parseInt()  //将字符串型转换为整型
        parseFloat()  //将字符串型转换为浮点型

        console.log('23' - '10' - 3)  //输出 number 10
        console.log('23' + '10' +3) //输出 string 23103

        let n = '1'+1
        n = n - 1;
        console.log(n)  //输出数字10

2.  数值型转换为字符串型

        .toString()

### 解构

在 ES5 中：如果计划从数组中提取特定元素，就需使用元素的索引，并将其保存到变量之中

        const arr = [2, 3, 4];
        const a = arr[0];
        const b = arr[1];
        const c = arr[2]

如果想对元素进行交换，需要引入一个临时变量

        const temp = arr[0];
        arr[0] = arr[1];
        arr[1] = temp;
        console.log(arr)   // [3,2,4]

在 ES6 中引入了解构的功能，以简化获取数组中数据的过程：

        const arr = [2,3,4];
        const [x, y, z] = = arr;
        console.log(x, y, z);

        const [x1, y1] = arr;
        console.log(x1, y1);  //只取前两个元素

        const[x2,,z2] = arr;
        console.log(x2, z2)  // 用逗号跳过元素

利用解构进行数组元素交换:

        const arr1 = [2, 3, 4];
        let [first, second] = arr1;
        [first, second] = [second, first];
        console.log(first, second); // 3,2
        console.log(arr1)   // still return 2,3,4

利用解构，让函数返回多个值

        const switchElement = function (a, b) {
        return [b, a];
        };

        const [item1, item2] = switchElement(1, 2);
        console.log(item1, item2);

利用解构设置默认值，通常用在 API 函数调用设置默认值：

        const [p = 1, q = 1, r = 1] = [2, 3];
        console.log(p, q, r);   // 2, 3, 1

在 Object 对象上使用解构:

        const restaurant = {
                name: 'Classico Italiano',
                location: 'Via Angelo Tavanti 23, Firenze, Italy',
                categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
        };
        const { name, categories } = restaurant;
        console.log(name, categories);

在 Object 上进行解构需要用大括号，并且变量名必须与 Object 中的属性名一致。  
也可以进行重命名。

        const { name: restaurantName, categories: tags } = restaurant;
        console.log(restaurantName, tags);

设置默认值:

        const { name: restaurantName = '', categories: tags = [], menu=[] } = restaurant;
        console.log(restaurantName, tags, menu);

嵌套

        const restaurant = {
                openingHours: {
                        thu: {
                                open: 12,
                                close: 22,
                        },
                        fri: {
                                open: 11,
                                close: 23,
                        },
                        sat: {
                                open: 0, // Open 24 hours
                                close: 24,
                        },
                },
        };

        const { openingHours } = restaurant;
        const { fri: { open, close } } = openingHours;
        console.log(open, close);

## 运算符

### 相等运算符

JavaScript 提供两种相等运算符：==和===。  
简单说，它们的区别是相等运算符（==）比较两个值是否相等，严格相等运算符（===）比较它们是否为“同一个值”。如果两个值不是同一类型，严格相等运算符（===）直接返回 false，而相等运算符（==）会将它们转换成同一个类型，再用严格相等运算符进行比较。

两个复合类型（对象、数组、函数）的数据比较时，不是比较它们的值是否相等，而是比较它们是否指向同一个地址。  
相等运算符会自动转换变量类型，造成很多意想不到的情况。建议不要使用相等运算符（==），只使用严格相等运算符（===）。

        18 === 18  // true
        '18' == 18  // true
        '18' === 18 // false

## 函数

在 JavaScript 中，使用函数前，必须用 function 关键字来定义函数。  
JavaScript 语言将函数看作一种值，与其它值（数值、字符串、布尔值等等）地位相同。凡是可以使用值的地方，就能使用函数。比如，可以把函数赋值给变量和对象的属性，也可以当作参数传入其他函数，或者作为函数的结果返回。函数只是一个可以执行的值，此外并无特殊之处。  
由于函数与其他数据类型地位平等，所以在 JavaScript 语言中又称函数为第一等公民。  
可以将函数作为变量传递给另一个变量

        const jonas = {
                year: 1991,
                calcAge: function() {
                        return 2023 - this.year;
                }
        }

        const f = jonas.calcAge;
        f();   // 会报错, 因为单独使用function，函数没有owner，导致this是undefined

函数表达式：

        const calAge = function(birthYear) {
                return 2023 - birthYear;
        }
        console.log(calAge(1991));

箭头函数:

        const calAge2 = birthYear => 2023 - birthYear;
        console.log(calAge2(1991));

        const yearsUntilRetirement = birthYear => {
                const age = 2023 - birthYear;
                const retirement = 65 - age;
                return retirement;
        }
        console.log(yearsUntilRetirement(1991));

注意： 箭头函数没有自己的 this 对象，而是使用 parent 的 this:

        const jonas = {
                firstName: 'Jonas',
                greet: () => console.log(`Hey ${this.firstName}`),
        }
        jonas.greet();   // console result: Hey undefined

箭头函数中 this 和 var 使用会产生奇怪效果：

        var firstName = 'Matilda';
        const jonas = {
                firstName: 'Jonas',
                greet: () => console.log(`Hey ${this.firstName}`),
        }
        jonas.greet();  // console result: Hey Matilda

对比以下两段代码：

        const jonas = {
                firstName: 'Jonas',
                year: 1995,
                calcAge: function() {
                        const isMillenial = function() {
                                console.log(this.year >=1991 & this.year <= 1996)
                        }
                        isMillenial();
                }
        }
        jonas.calcAge();  // 会报错, this is undefined

使用箭头函数

        const jonas = {
                firstName: 'Jonas',
                year: 1995,
                calcAge: function() {
                        const isMillenial = () => {
                                console.log(this.year >=1991 & this.year <= 1996)
                        }
                        isMillenial();
                }
        }
        jonas.calcAge(); // 箭头函数继承了parent的this，能正常输出

#### 参数传递方式

函数参数如果是原始类型的值（数值、字符串、布尔值），传递方式是传值传递（passes by value）。这意味着，在函数体内修改参数值，不会影响到函数外部。

        let p = 2;
        function f(p) {
            p = 3;
        }
        f(p);   p // 2

如果函数参数是复合类型的值（数组、对象、其他函数），传递方式是传址传递（pass by reference）。也就是说，传入函数的原始值的地址，因此在函数内部修改参数，将会影响到原始值。

        let obj = { p: 1 };
        function f(o) {
            o.p = 2;
        }
        f(obj);
        obj.p // 2

#### arguments 对象

arguments 对象包含了函数运行时的所有参数，这个对象只有在函数体内部，才可以使用。

        let f = function (one) {
                console.log(arguments[0]);
                console.log(arguments[1]);
                console.log(arguments[2]);
        }
        f(1, 2, 3)
        // 1
        // 2
        // 3

虽然 arguments 很像数组，但它是一个对象。数组专有的方法（比如 slice 和 forEach），不能在 arguments 对象上直接使用。

#### 闭包

闭包是“定义在一个函数内部的函数”。闭包最大的特点，就是它可以“记住”诞生的环境，比如 f2 记住了它诞生的环境 f1，所以从 f2 可以得到 f1 的内部变量。在本质上，闭包就是将函数内部和函数外部连接起来的一座桥梁。  
闭包的最大用处有两个，一个是可以读取函数内部的变量，另一个就是让这些变量始终保持在内存中，即闭包可以使得它诞生环境一直存在。

        function createIncrementor(start) {
            return function () {
                return start++;
            };
        }
        let inc = createIncrementor(5);
        inc() // 5
        inc() // 6
        inc() // 7

闭包的另一个用处，是封装对象的私有属性和私有方法。

        function Person(name) {
                let _age;
                function setAge(n) {
                        _age = n;
                }
                function getAge() {
                        return _age;
                }

                return {
                        name: name,
                        getAge: getAge,
                        setAge: setAge
                };
        }
        let p1 = Person('张三');
        p1.setAge(25);
        p1.getAge() // 25

## 面向对象

JavaScript 语言的对象体系，不是基于“类”的，而是基于构造函数（constructor）和原型链（prototype）。  
构造函数就是一个普通的函数，但是有自己的特征和用法。

        let Vehicle = function () {
            this.price = 1000;
        };
        let v = new Vehicle();
        v.price // 1000

#### 原型对象 rototype

#### 原型链

### 异步操作

异步操作的几种模式：

1.  回调函数

        function f1(callback) {
            // ...
            callback();
        }
        function f2() {
            // ...
        }
        f1(f2);

    回调函数的优点是简单、容易理解和实现，缺点是不利于代码的阅读和维护，各个部分之间高度耦合（coupling），使得程序结构混乱、流程难以追踪（尤其是多个回调函数嵌套的情况），而且每个任务只能指定一个回调函数。

2.  事件监听  
    另一种思路是采用事件驱动模式。异步任务的执行不取决于代码的顺序，而取决于某个事件是否发生。

           f1.on('done', f2);
           function f1() {
               setTimeout(function () {
                   // ...
                   f1.trigger('done');
               }, 1000);
           }

    这种方法的优点是比较容易理解，可以绑定多个事件，每个事件可以指定多个回调函数，而且可以“去耦合”（decoupling），有利于实现模块化。缺点是整个程序都要变成事件驱动型，运行流程会变得很不清晰。阅读代码的时候，很难看出主流程。

3.  发布/订阅  
    下面采用的是 Ben Alman 的 Tiny Pub/Sub，这是 jQuery 的一个插件。

            // f2向信号中心jQuery订阅done信号
            jQuery.subscribe('done', f2);

            function f1() {
                setTimeout(function () {
                    // ...
                    jQuery.publish('done');
                }, 1000);
            }

            // f2完成执行后，可以取消订阅（unsubscribe）。
            jQuery.unsubscribe('done', f2);

#### 定时器

1.  setTimeout()  
    setTimeout 函数用来指定某个函数或某段代码，在多少毫秒之后执行。

            let timerId = setTimeout(func|code, delay);

2.  setInterval()  
    setInterval 函数的用法与 setTimeout 完全一致，区别仅仅在于 setInterval 指定某个任务每隔一段时间就执行一次，也就是无限次的定时执行。

3.  clearTimeout()，clearInterval()

        let id1 = setTimeout(f, 1000);
        let id2 = setInterval(f, 1000);
        clearTimeout(id1);
        clearInterval(id2);

#### Promise

Promise 对象是 JavaScript 的异步操作解决方案，为异步操作提供统一接口。它起到代理作用（proxy），充当异步操作与回调函数之间的中介，使得异步操作具备同步操作的接口。

        function f1(resolve, reject) {
            // 异步代码...
        }
        let p1 = new Promise(f1);
        p1.then(f2);

Promise 对象通过自身的状态，来控制异步操作。Promise 实例具有三种状态。

        异步操作未完成（pending）
        异步操作成功（fulfilled）
        异步操作失败（rejected）

Promise 实例的 then 方法，用来添加回调函数。  
then 方法可以接受两个回调函数，第一个是异步操作成功时（变为 fulfilled 状态）的回调函数，第二个是异步操作失败（变为 rejected）时的回调函数（该参数可以省略）。一旦状态改变，就调用相应的回调函数。

微任务  
Promise 的回调函数属于异步任务，会在同步任务之后执行。  
但是，Promise 的回调函数不是正常的异步任务，而是微任务（microtask）。它们的区别在于，正常任务追加到下一轮事件循环，微任务追加到本轮事件循环。这意味着，微任务的执行时间一定早于正常任务。

        setTimeout(function() {
            console.log(1);
        }, 0);

        new Promise(function (resolve, reject) {
            resolve(2);
        }).then(console.log);

        console.log(3);
        // 3
        // 2
        // 1

### 窗口对象

在 JavaScript 中，一个浏览器窗口就是一个 window 对象。window 对象主要用来控制由窗口弹出的对话框、打开窗口或关闭窗口、控制窗口的大小和位置等等。

#### 打开窗口

        window.open(URL, 窗口名称, 参数);

URL：指的是打开窗口的地址，窗口名称：指的是 window 对象的名称，可以是 a 标签或 form 标签中 target 属性值。如果指定的名称是一个已经存在的窗口名称，则返回对该窗口的引用，而不会再新打开一个窗口。  
参数：对打开的窗口进行属性设置。

    // 打开一个指定位置的窗口：
    window.open("www.google.com","","top=200,left=200");
    // 打开一个指定大小的窗口：
    window.open("www.google.com","","width=200,height=200");
    // 打开一个固定大小的窗口：
    window.open("www.google.com","","width=200,height=200,resizable");

其他常用方法：

    open()、close()	//打开窗口、关闭窗口
    resizeBy()、resizeTo()	//改变窗口大小
    moveBy()、moveTo()	//移动窗口
    setTimeout(code, time)、clearTimeout()	//设置或取消“一次性”执行的定时器
    setInterval()、clearInterval()	//设置或取消“重复性”执行的定时器

#### 窗口历史

history 对象属性：

        current	//当前窗口的URL
        next	//历史列表中的下一个URL
        previous	//历史列表中的前一个URL
        length	//历史列表的长度，用于判断列表中的入口数目

history 对象方法:

    go()	//进入指定的网页
    back()	//返回上一页
    forward()	//进入下一页

常见的“上一页”与“下一页”实现代码如下：

    <a href="javascript:window.history.forward();">下一页</a>
    <a href="javascript:window.history.back();">上一页</a>

### 对话框

在 JavaScript 中，对话框共有 3 种，这 3 种对话框分别使用以下 3 种方法定义：

    alert(message)； // 弹出一个提示框
    confirm(message)；  // 用于确认信息，它只有一个参数，返回值为true或false
    prompt(message)；  // 用于输入并返回用户输入的字符串

### 文档对象

document 对象是 window 对象中的子对象。

1.  document 对象属性

        title	文档标题，即title标签内容
        URL	文档地址
        fileCreateDate	文档创建日期
        fileModifiedDate	文档修改时间（精确到天）
        lastModified	文档修改时间（精确到秒）
        fileSize	文档大小
        fgColor	定义文档的前景色
        bgColor	定义文档的背景色
        linkColor	定义“未访问”的超链接颜色
        alinkColor	定义“被激活”的超链接颜色
        vlinkColor	定义“访问过”的超链接颜色

2.  document 对象方法

        document.write()	输入文本到当前打开的文档
        document.writeIn()	输入文本到当前打开的文档，并添加换行符“\n”
        document.getElementById()	获取某个id值的元素
        document.getElementsByName()	获取某个name值的元素，用于表单元素

### DOM 对象

DOM，全称“Document Object Model（文档对象模型）”，它是由 W3C 组织定义的一个标准。  
在前端开发时，我们往往需要在页面某个地方添加一个元素或者删除元素，这种添加元素、删除元素的操作就是通过 DOM 来实现的。说白了，DOM 就是一个接口，我们可以通过 DOM 来操作页面中各种元素，例如添加元素、删除元素、替换元素等。

1.  DOM 节点属性

        parentNode	获取当前节点的父节点
        childNodes	获取当前节点的子节点集合
        firstChild	获取当前节点的第一个子节点
        lastChild	获取当前节点的最后一个子节点
        previousSibling	获取当前节点的前一个兄弟节点
        nextSibling	获取当前节点的后一个兄弟节点
        attributes	元素的属性列表

2.  DOM 节点操作

        let e = document.createElement("元素名");
        obj.appendChild(new)
        obj.insertBefore(new,ref)
        obj.removeChild(oldChild);
        obj.style.属性名;       // 操作CSS样式

    操作实例：

        let ccontent = document.createElement("div");
        ccontent.className = "box";
        ccontent.style.position = "absolute";
        ccontent.style.top = "10px";
        ccontent.style.left = "10px";
        cparent.appendChild(ccontent);

3.  选择节点

        document.querySelector('.message').textContent

4.  添加事件

        document.querySelector('.btnCheck').addEventListener('click', function () {
                console.log(document.querySelector('.guess').value);
        });

监听键盘 keydown 事件：

        document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape') {
                        console.log('ESC is pressed!');
                }
        });

### 事件

在 JavaScript 中，事件往往是页面的一些动作引起的，例如当用户按下鼠标或者提交表单，甚至在页面移动鼠标时，事件都会出现。  
在 JavaScript 中，调用事件的方式共有 2 种：

1.  在 script 标签中调用；

        let e = document.getElementById("btn");
        e.onclick = function () {
                    alert("button clicked");
        }

        document.getElementById("btn1").addEventListener("mouseover", showType);
        function showType(event){
            alert(event.type);
            alert(event.target);
        }

2.  在元素中调用；

        <body>
                <input type="button" onclick="alert('button clicked')" value="按钮"/>
        <body>

#### 鼠标事件

        onclick	鼠标单击事件
        ondbclick	鼠标双击事件
        onmouseover	鼠标移入事件
        onmouseout	鼠标移出事件
        onmousemove	鼠标移动事件
        onmousedown	鼠标按下事件
        onmouseup	鼠标松开事件

#### 键盘事件

        onkeydown	按下键事件（包括数字键、功能键）
        onkeypress	按下键事件（只包含数字键）
        onkeyup	放开键事件（包括数字键、功能键）

#### 页面相关事件

        onload	页面加载事件
        onresize	页面大小事件
        onerror	页面或图片加载出错事件
