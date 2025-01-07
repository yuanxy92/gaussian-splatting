python train.py \
-s /data/hdd/Data/SkinSight_video/UVC_cam_undis \
-d /data/hdd/Data/SkinSight_video/UVC_cam_undis/depths \
-m /data/hdd/Data/SkinSight_video/UVC_cam_undis/3dgs_trans \
-r 1

python utils/make_depth_scale.py --base_dir /data/hdd/Data/SkinSight_video/UVC_cam_undis --depths_dir /data/hdd/Data/SkinSight_video/UVC_cam_undis/depths
python train.py \
-s /data/hdd/Data/SkinSight_video/UVC_cam_undis \
-d /data/hdd/Data/SkinSight_video/UVC_cam_undis/depths \
-m /data/hdd/Data/SkinSight_video/UVC_cam_undis/3dgs_trans_v2 \
-r 1


python render.py \
-s /data/hdd/Data/SkinSight_video/UVC_cam_undis \
-m /data/hdd/Data/SkinSight_video/UVC_cam_undis/3dgs \
-r 1


python train.py \
-s /data/hdd/Data/SkinSight_video/nature_hololens/colmap \
-m /data/hdd/Data/SkinSight_video/nature_hololens/colmap/3dgs \
-r 1

python render.py \
-s /data/hdd/Data/SkinSight_video/nature_hololens/colmap \
-m /data/hdd/Data/SkinSight_video/nature_hololens/colmap/3dgs \
-r 1


python train.py \
-s /data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense \
-m /data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense/3dgs \
-r 1

python render.py \
    -s /data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense \
    -m /data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense/3dgs \
    --begin_index 0 --image_num 450 -r 1

python render.py \
    -s /data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense \
    -m /data/hdd/Data/SkinSight_video/nature_hololens/colmap_dense/3dgs \
    --begin_index 450 --image_num 450 -r 1