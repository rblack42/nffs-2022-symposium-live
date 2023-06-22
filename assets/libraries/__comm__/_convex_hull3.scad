function is_zero(p) = p == [0, 0, 0];

function _cmp(a, b) =
    let(
        ax = a[0], ay = a[1], az = a[2],
        bx = b[0], by = b[1], bz = b[2]
    )
    ax != bx ? ax < bx : 
    ay != by ? ay < by :
    az < bz;
    
function _convex_hull_sort_by_xyz(pts) = 
    let(leng = len(pts))
    leng <= 1 ? pts : 
        let(
            pivot = pts[0],
            before = [for(j = 1; j < leng; j = j + 1) if(_cmp(pts[j], pivot)) pts[j]],
            after =  [for(j = 1; j < leng; j = j + 1) if(!_cmp(pts[j], pivot)) pts[j]]
        )
        concat(_convex_hull_sort_by_xyz(before), [pivot], _convex_hull_sort_by_xyz(after));

function normal(pts, f) = cross(pts[f[1]] - pts[f[0]], pts[f[2]] - pts[f[0]]);

function _fst_v1(pts, leng, i) =
    i != leng && is_zero(pts[i] - pts[0]) ? _fst_v1(pts, leng, i + 1) : i;
  
function _fst_v2(pts, leng, v1, i) = 
    i != leng && is_zero(cross(pts[v1] - pts[0], pts[i] - pts[0])) ? _fst_v2(pts, leng, v1, i + 1) : i;

function _fst_v3(pts, leng, n, d, i) =
    i == leng ? [i, d]:
    let(nd = n *(pts[i] - pts[0]))
    nd == 0 ? _fst_v3(pts, leng, n, nd, i + 1) : 
    [i, nd];

function m_assign(m, i, j, v) =
    let(
        lt = m[i],
        leng_lt = len(lt),
        nlt = concat(
            j == 0 ? [] : [for(idx = [0:j - 1]) lt[idx]],
            [v],
            j == leng_lt - 1 ? [] : [for(idx = [j + 1:leng_lt - 1]) lt[idx]]
        ),
        leng_m = len(m)
    )
    concat(
        i == 0 ? [] : [for(idx = [0:i - 1]) m[idx]],
        [nlt],
        i == leng_m - 1 ? [] : [for(idx = [i + 1:leng_m - 1]) m[idx]]
    );

function next_vis(i, pts, cur_faces, cur_faces_leng, next, vis, j = 0) = 
    j == cur_faces_leng ? [next, vis] :
    let(
        f = cur_faces[j],
        d = (pts[f[0]] - pts[i]) * normal(pts, f),
        nx = d >= 0 ? concat(next, [f]) : next,
        s = d > 0 ? 1 :
            d < 0 ? -1 : 0,
        vis1 = m_assign(vis, f[0], f[1], s),
        vis2 = m_assign(vis1, f[1], f[2], s),
        vis3 = m_assign(vis2, f[2], f[0], s)
    )
    next_vis(i, pts, cur_faces, cur_faces_leng, nx, vis3, j + 1);
    
function next2(i, cur_faces, cur_faces_leng, vis, next, j = 0) = 
    j == cur_faces_leng ? next : 
    let(
        f = cur_faces[j],
        a = f[0],
        b = f[1],
        c = f[2],
        nx1 = vis[a][b] < 0 && vis[a][b] != vis[b][a] ? 
            concat(next, [[a, b, i]]) : next,
        nx2 = vis[b][c] < 0 && vis[b][c] != vis[c][b] ? 
            concat(nx1, [[b, c, i]]) : nx1,        
        nx3 = vis[c][a] < 0 && vis[c][a] != vis[a][c] ? 
            concat(nx2, [[c, a, i]]) : nx2                    
    )
    next2(i, cur_faces, cur_faces_leng, vis, nx3, j + 1);

function _all_faces(v0, v1, v2, v3, pts, pts_leng, vis, cur_faces, i = 0) =
    i == pts_leng ? cur_faces :
    i == v0 || i == v1 || i == v2 || i == v3 ? _all_faces(v0, v1, v2, v3, pts, pts_leng, vis, cur_faces, i + 1) :
    let(
        cur_faces_leng = len(cur_faces),
        nv = next_vis(i, pts, cur_faces, cur_faces_leng, [], vis),
        nx1 = nv[0],
        vis1 = nv[1],
        nx2 = next2(i, cur_faces, cur_faces_leng, vis1, nx1)
    )
    _all_faces(v0, v1, v2, v3, pts, pts_leng, vis1, nx2, i + 1);

function _convex_hull3(pts) = 
    let(
        sorted = _convex_hull_sort_by_xyz(pts),
        leng = len(sorted),
        v0 = 0,
        v1 =  _fst_v1(sorted, leng, v0 + 1),
        _ = assert(v1 < leng, "common points"),
        v2 = _fst_v2(sorted, leng, v1, v1 + 1),
        __ = assert(v2 < leng, "collinear points"),
        n = cross(sorted[v1] - sorted[v0], sorted[v2] - sorted[v0]),
        v3_d = _fst_v3(sorted, leng, n, 0, v2 + 1),
        v3 = v3_d[0],
        ___ = assert(v3 < leng, "coplanar points"),
        d = v3_d[1],
        fst_tetrahedron = d > 0 ? [
                [v1, v0, v2],
                [v0, v1, v3],
                [v1, v2, v3],
                [v2, v0, v3]
            ] 
            : 
            [
                [v0, v1, v2],
                [v1, v0, v3],
                [v2, v1, v3],
                [v0, v2, v3]
            ],
        init_vis = [for(i = [0:leng - 1]) [for(j = [0:leng - 1]) 0]],
        faces = _all_faces(v0, v1, v2, v3, sorted, leng, init_vis, fst_tetrahedron), // counter-clockwise
        reversed = [for(face = faces)      // OpenSCAD prefers clockwise.
            [for(i = 2; i >= 0; i = i - 1)
                 face[i]]
        ]
    )
    [
        sorted,
        reversed   
    ];