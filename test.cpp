#include<iostream>
#include<vector>
#include<string>
#include<array>

class A
{
private:
    static int pri_sta;
    int pri1;
public:
    static int pub_sta;
    int pub1;
    A():pri1{0},pub1{0}{};
    A(int i):pri1{i},pub1{i}{};
    ~A(){};
    void get();
    void set();
    A& operator=(const A& arg)
    {
        pri1 = arg.pri1;
        pub1 = arg.pub1;

        return  *this;
    }
};

void A::get()
{
    std::cout << "get pri_sta:" << pri_sta << std::endl;
    std::cout << "get pri1:" << pri1 << std::endl;

    std::cout << "get pub_sta:" << pub_sta << std::endl;
    std::cout << "get pub1:" << pub1 << std::endl;
}

void A::set()
{
    std::cout << "set pri_sta:";
    std::cin >> pri_sta;

    std::cout << "set pri1:";
    std::cin >> pri1;

    std::cout << "set pub1:";
    std::cin >> pub1;
}

int A::pri_sta = 0;
int A::pub_sta = 0;

template <typename T>
T sum(T a,T b)
{
    a = a + b;
    return a;
}

template <typename T>
class test
{
private:
    /* data */
public:
    test(/* args */);
    ~test();
};

template <typename T>
test<T>::test(/* args */)
{
}

template <typename T>
test<T>::~test()
{
}


#include <iostream>
using namespace std;

struct S
{
    char a;     // 位置1：1字节
    int b : 5;  // 位置2：4字节（int）
    int c : 11, // 位置2续
          : 0,  // 分割位置2
        d : 8;  // 位置3：4字节（int）
    struct
    {
        int ee : 8; // 位置4：4字节（int）
    } e;
} obj;

int main()
{
    using namespace std;
    using std::cin;

    using INT = int;
    typedef int INT;

    // A a(2);
    // A b(3);
    // A& c = b;

    // c.get();

    // int A::* pub1 = &A::pub1;
    // std::cout << a.*pub1 << std::endl;
    // std::cout << b.*pub1 << std::endl;

    // std::cout << A::pub_sta << std::endl;
    // std::cout << a.pub_sta << std::endl;
    // std::cout << b.pub_sta << std::endl;
    
    // a = b;

    // a.get();
    // b.get();

    // a.set();

    // b = a;

    // A::pub_sta = 0;
    
    // a.get();
    // b.get();

    // 输出结构体总大小：1 + (3填充) + 4 + 4 + 4 = 16字节（GCC 64位）
    cout << "sizeof(S) = " << sizeof(S) << endl;
    // 验证嵌套结构体大小：4字节（int）
    cout << "sizeof(obj.e) = " << sizeof(obj.e) << endl;

    cout << "a = " << obj.a << endl;
    cout << "b = " << obj.b << endl;
    cout << "c = " << obj.c << endl;
    cout << "d = " << obj.d << endl;

    cout << __LINE__ << endl;
    cout << __FILE__ << endl;
    cout << __DATE__ << endl;
    cout << __TIME__ << endl;
    cout << __FUNCTION__ << endl;

    int num = 0;
    int* pnum = &num;

    int anum[10] = {0};
    int* apnum[10] = {pnum};
    int (*panum)[10] = &anum;

    
    int *pnew = nullptr;
    pnew = new int (9);
    std::cout << *pnew << std::endl;
    std::cout << pnew << std::endl;
    delete pnew;

    int *panew = new int[10] {0,1,2,3,4,5,6,7,8,9};
    int arr[] = {0,1,2,3,4,5,6,7,8,9}; 
    for (auto i : arr)
    {
       std::cout << i << std::endl;
    }
    
    std::cout << panew[0] << std::endl;
    std::cout << panew[9] << std::endl;
    delete[] panew;


    vector<int> vec {0,1,2,3,4,5,6,7,8};
    // 引用遍历，不拷贝元素，可加const表示仅读取（推荐）
    for (const auto& num : vec) {
        cout << num << " ";
    }

    string str {"01234567\n"};
    std::cout << str << std::endl;

    // array<int,10> arr;

    return 0;
}
