#include <iostream>

using namespace std;
class Rectangle {
public:
    virtual void display() const {
        cout << width << ' ' << height << endl;
    }
    
protected:
    int width;
    int height;
};

class RectangleArea : public Rectangle {
public:
    void display() const override {
        cout << (width * height) << endl;
    }
    
    void read_input() {
        cin >> width >> height;
    }
};


int main()
{
    
    RectangleArea r_area;

    r_area.read_input();

    r_area.Rectangle::display();

    r_area.display();
    
    return 0;
}
