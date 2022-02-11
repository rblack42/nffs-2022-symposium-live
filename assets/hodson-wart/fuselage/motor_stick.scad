include <../wart_data.scad>
use <magik/rounded_post.scad>
include <colors.scad>

module motor_stick() {
    color(WOOD_Balsa)
        rotate([90,0,0])
            translate([0,0,-ms_y/2])
                linear_extrude(height = ms_y, convexity=10)
                    polygon(ms_poly);

    // add front wing posts
    translate([ms_x4,-ms_y/2-spar_size/2])
      color(WOOD_Birch)
        rounded_post(
          z1=wing_post_height,
          z2 = wing_post_height - pt_h,
          t = spar_size
        );
    // add rear wing post
  translate([ms_x3,-ms_y/2-spar_size/2])
      color(WOOD_Birch)
        rounded_post(
          z1=wing_post_height,
          z2 = wing_post_height - pt_h,
          t = spar_size
        );
}

motor_stick();