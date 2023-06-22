//################################################################
// paper tube.scad - creates simple hollow cylinder
// (c) 2021 - Roie R. Black
// docs: https://rblack.github.io/math-magik/magik/paper_tube.html

$fn = 100;

module paper_tube(r=1, h=2, t=0.25) {
  th = 3 * h;
  difference() {
    cylinder(r=r+t,h=h);
    translate([0,0,-h])
      cylinder(r=r, h=th);
  }
}

paper_tube();
