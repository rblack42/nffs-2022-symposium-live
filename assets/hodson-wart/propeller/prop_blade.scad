include <./wart_blade.scad>
include <MMlib/colors.scad>

sf = 0.3202;

module prop_blade() {
  color(WOOD_Balsa) {
    translate([0,0,0])
    rotate([0,-90,-90])
    linear_extrude(
            height = 1/32,
            center = false,
            convexity = 10)
        scale([sf,sf])
            polygon(wart_coords);
    }
}

prop_blade();
