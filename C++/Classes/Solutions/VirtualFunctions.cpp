#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

class Person
{
    public:
        string name;
        int age;

        virtual void getdata(){}
        virtual void putdata(){}
};

class Student: public Person
{
    private:
        int marks[6];
        int cur_id;
        static int seq_st_id;

    public:
        Student() 
        { 
            this->cur_id = ++seq_st_id; 
        }

        void getdata() override
        {
            cin >> name >> age;
            for (int i = 0; i < 6; i++) 
            {
                cin >> marks[i];
            }
        }

        void putdata() override
        {
            int sum = accumulate(marks, marks + 6, 0);
            cout << name << " " << age << " " << sum << " " << cur_id << endl;
        }
};

int Student::seq_st_id = 0;

class Professor: public Person
{
    private:
        int publications;
        int cur_id;
        static int seq_prof_id;

    public:
        Professor()
        {
            this->cur_id = ++seq_prof_id;
        }

        void getdata() override
        {
            cin >> name >> age >> publications;
        }

        void putdata() override
        {
            cout << name << " " << age << " " << publications << " " << cur_id << endl;
        }
};

int Professor::seq_prof_id = 0;

int main()
{
    int n, val;
    cin >> n; //The number of objects that is going to be created.
    Person *per[n];

    for (int i = 0;i < n;i++)
    {

        cin >> val;
        if (val == 1)
        {
            // If val is 1 current object is of type Professor
            per[i] = new Professor;
        }
        else
        {
            per[i] = new Student; // Else the current object is of type Student
        } 

        per[i]->getdata(); // Get the data from the user.
    }

    for (int i = 0; i < n; i++)
    {
        per[i]->putdata(); // Print the required output for each object.
    }

    return 0;

}
