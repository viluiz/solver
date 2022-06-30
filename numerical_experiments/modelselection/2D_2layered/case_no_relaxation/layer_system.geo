//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0.0, 10.0, 0, 1.0};
//+
Point(3) = {0.0, 20.0, 0, 1.0};
//+
Point(4) = {100.0, 10.0, 0, 1.0};
//+
Point(5) = {100.0, 20.0, 0, 1.0};
//+
Point(6) = {100., 0., 0, 1.0};
//+
Line(1) = {3, 5};
//+
Line(2) = {5, 4};
//+
Line(3) = {4, 6};
//+
Line(4) = {6, 1};
//+
Line(5) = {1, 2};
//+
Line(7) = {2, 3};
//+
Line(8) = {2, 4};
//+
Line Loop(1) = {1, 2, -8, 7};
//+
Plane Surface(1) = {1};
//+
Line Loop(2) = {8, 3, 4, 5};
//+
Plane Surface(2) = {2};
//+
Physical Line(1) = {1, 4}; //sides
//+
Physical Line(2) = {7, 5}; //left
//+
Physical Line(3) = {2, 3}; //right
//+
Physical Surface(4) = {1}; //top
//+
Physical Surface(5) = {2}; //bottom

Mesh.Algorithm = 1;
Mesh.MshFileVersion = 2;
Mesh.RecombinationAlgorithm = 0;
Mesh.CharacteristicLengthMin = 0.1;
Mesh.CharacteristicLengthMax = 1.0;
