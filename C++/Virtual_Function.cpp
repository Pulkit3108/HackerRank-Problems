#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int pid = 1;
int sid = 1;

class Person {
  protected:
    char name[101];
    int age, id;
  public:
    virtual void getdata(){};
    virtual void putdata(){};
};

class Professor : public Person {
    
    public:
        int publications;
    
        Professor() {
            id = pid++;
        }
    
        void getdata() override {
            cin >> name;
            cin >> age;
            cin >> publications;
        }
    
        void putdata() override {
            cout << name << " " << age << " " << publications << " " << id << endl;
        }
};

class Student : public Person {
    public:
        int score;
        int id;
    
        Student() {
            id = sid++;
        }
    
        void getdata() override {
            cin >> name;
            cin >> age;
            int num = 0;
            for(int i = 0; i < 6; i++) {
                int t;
                cin >> t;
                num += t;
            }
            score = num;
        }

        void putdata() override {
            cout << name << " " << age << " " << score << " " << id << endl;
        }
};
int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
