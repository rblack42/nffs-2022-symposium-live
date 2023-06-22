
module covering_generator(points, thickness) {


    function reverse(lt) = [for(i = len(lt) - 1; i >= 0; i = i - 1) lt[i]];

    rows = len(points);
    columns = len(points[0]);

    yi_range = [0:rows - 2];
    xi_range =  [0:columns - 2];

    function xy_to_index(x, y, columns) = y * columns + x;

    top_pts = [
        for(row_pts = points)
            for(pt = row_pts)
                pt
    ];

    base_pts = [
        for(pt = top_pts)
            [pt[0], pt[1], pt[2] - thickness]
    ];

    leng_pts = len(top_pts);

    top_tri_faces1 =  [
        for(yi = yi_range)
            for(xi = xi_range)
                [
                    xy_to_index(xi, yi, columns),
                    xy_to_index(xi + 1, yi + 1, columns),
                    xy_to_index(xi + 1, yi, columns)
                ]
    ];

    top_tri_faces2 = [
        for(yi = yi_range)
            for(xi = xi_range)
                [
                    xy_to_index(xi, yi, columns),
                    xy_to_index(xi, yi + 1, columns),
                    xy_to_index(xi + 1, yi + 1, columns)
                ]
    ];

    offset_v = [leng_pts, leng_pts, leng_pts];
    base_tri_faces1 = [
        for(face = top_tri_faces1)
            reverse(face) + offset_v
    ];

    base_tri_faces2 = [
        for(face = top_tri_faces2)
            reverse(face) + offset_v
    ];

    side_faces1 = [
        for(xi = xi_range)
            let(
                idx1 = xy_to_index(xi, 0, columns),
                idx2 = xy_to_index(xi + 1, 0, columns)
            )
            [
                idx1,
                idx2,
                idx2 + leng_pts,
                idx1 + leng_pts
            ]
    ];

    side_faces2 = [
        for(yi = yi_range)
            let(
                xi = columns - 1,
                idx1 = xy_to_index(xi, yi, columns),
                idx2 = xy_to_index(xi, yi + 1, columns)
            )
            [
                idx1,
                idx2,
                idx2 + leng_pts,
                idx1 + leng_pts
            ]
    ];

    side_faces3 = [
        for(xi = xi_range)
            let(
                yi = rows - 1,
                idx1 = xy_to_index(xi, yi, columns),
                idx2 = xy_to_index(xi + 1, yi, columns)
            )
            [
                idx2,
                idx1,
                idx1 + leng_pts,
                idx2 + leng_pts
            ]
    ];

    side_faces4 = [
        for(yi = yi_range)
            let(
                idx1 = xy_to_index(0, yi, columns),
                idx2 = xy_to_index(0, yi + 1, columns)
            )
            [
                idx2,
                idx1,
                idx1 + leng_pts,
                idx2 + leng_pts
            ]
    ];

    pts = concat(top_pts, base_pts);
    face_idxs = concat(
            top_tri_faces1, top_tri_faces2,
            base_tri_faces1, base_tri_faces2,
            side_faces1,
            side_faces2,
            side_faces3,
            side_faces4
        );

    polyhedron(
        points = pts,
        faces = face_idxs
    );
}
