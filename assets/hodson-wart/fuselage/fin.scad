include <../wart_data.scad>
use <magik/curved_spar.scad>
include <colors.scad>

module fin() {
  color(WOOD_Balsa)
    rotate([90,0,0]) {
      curved_spar( r=2, dr = 1/16, t=1/16, a1=90, a2=180);
      cube([1/16, 2, 1/16]);
    }
}

fin();