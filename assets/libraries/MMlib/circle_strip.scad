//#####################################
// circle_strip
// (c) 2021 - Roie R. Black
//=====================================
$fn = 100;


module circle_strip(r=3, t=0.5) {
  difference() {
    circle(r);
    circle(r-t);
  }
}

circular_strip();
