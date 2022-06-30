//+
Point(1) = {0., 0., 0., 1.0};
//+
Point(2) = {0., 10., 0, 1.0};
//+
Point(3) = {0., 20., 0, 1.0};
//+
Point(4) = {50., 20., 0, 1.0};
//+
Point(5) = {100., 20., 0, 1.0};
//+
Point(6) = {100., 10., 0, 1.0};
//+
Point(7) = {100., 0., 0, 1.0};
//+
Point(8) = {50., 0., 0, 1.0};
//+
Point(9) = {50., 10., 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 5};
//+
Line(5) = {6, 5};
//+
Line(6) = {7, 6};
//+
Line(7) = {8, 7};
//+
Line(8) = {1, 8};
//+
Line(9) = {2, 9};
//+
Line(10) = {9, 6};
//+
Line(11) = {8, 9};
//+
Line(12) = {9, 4};
//+
Line Loop(1) = {2, 3, -12, -9};
//+
Plane Surface(1) = {1};
//+
Line Loop(2) = {12, 4, -5, -10};
//+
Plane Surface(2) = {2};
//+
Line Loop(3) = {1, 9, -11, -8};
//+
Plane Surface(3) = {3};
//+
Line Loop(4) = {11, 10, -6, -7};
//+
Plane Surface(4) = {4};
//+
Physical Line(1) = {3, 4, 8, 7}; //sides
//+
Physical Line(2) = {1, 2}; //left
//+
Physical Line(3) = {5, 6}; //right
//+
Physical Surface(4) = {1}; //top left
//+
Physical Surface(5) = {2}; //top right
//+
Physical Surface(6) = {3}; //bottom left
//+
Physical Surface(7) = {4}; //bottom right

Mesh.Algorithm = 1;
Mesh.MshFileVersion = 2;
Mesh.RecombinationAlgorithm = 0;
Mesh.CharacteristicLengthMin = 0.1;
Mesh.CharacteristicLengthMax = 1.0;
