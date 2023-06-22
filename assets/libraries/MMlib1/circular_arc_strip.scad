//#####################################
// circular_arc_strip
// (c) 2021 - Roie R. Black
//=====================================
$fn = 100;
use <MMlib/circle_strip.scad>


module circular_arc_strip(
    r=3,
    start_angle=0, end_angle=270,
    t=0.5
  ) {
  dang = (end_angle-start_angle)/4;
  a0 = start_angle;
  a1 = a0 + dang;
  a2 = a1 + dang;
  a3 = a2 + dang;
  a4 = a3 + dang;
  pr = r * sqrt(2) + 1;
  intersection() {
    polygon([
      [0,0],
      [pr*cos(a0), pr*sin(a0)],
      [pr*cos(a1), pr*sin(a1)],
      [pr*cos(a2), pr*sin(a2)],
      [pr*cos(a3), pr*sin(a3)],
      [pr*cos(a4), pr*sin(a4)],
      [0,0]
    ]);
    circle_strip(r,t);
  }
}

circular_arc_strip();
