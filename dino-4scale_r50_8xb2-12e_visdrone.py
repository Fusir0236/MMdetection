_base_ = 'dino-4scale_r50_8xb2-12e_coco.py'

model = dict(
    bbox_head=dict(
        type='DINOHead',
        num_classes=5,
    )
)

# 修改数据集相关配置
data_root ='S:/PyCharm Community Edition 2021.3.1/project-python/mmdetection/data/coco/'
metainfo = {
    'classes':
        ('id1', 'id2', 'id3', 'id4', 'id5',),
    # 更换自己的数据类别名，我是5分类
    # palette is a list of color tuples, which is used for visualization.
    'palette':
        [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 228), ]
}

train_dataloader = dict(
    batch_size=2,
    num_workers=2,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/train.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    batch_size=2,
    num_workers=2,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/val.json',
        data_prefix=dict(img='valid/')))
test_dataloader = dict(
    batch_size=2,
    num_workers=2,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/test.json',
        data_prefix=dict(img='test/')))

# 修改评价指标相关配置
val_evaluator = dict(ann_file=data_root + 'annotations/val.json')
test_evaluator = dict(ann_file=data_root + 'annotations/test.json')


# optim_wrapper = dict(type='AmpOptimWrapper')

default_hooks = dict(logger=dict(type='LoggerHook', interval=200))

# load_from = 'pth_dir/dino-4scale_r50_8xb2-12e_coco_20221202_182705-55b2bba2.pth'

# python tools/train.py configs/dino/dino-4scale_r50_8xb2-12e_visdrone.py
# python tools/test.py configs/dino/dino-4scale_r50_8xb2-12e_visdrone.py work_dirs/tood_r50_fpn_1x_visdrone/epoch_12.pth --show --show-dir test_save
# python tools/test.py configs/dino/dino-4scale_r50_8xb2-12e_visdrone.py work_dirs/tood_r50_fpn_1x_visdrone/epoch_12.pth --tta


# python tools/test.py configs/dino/dino-4scale_r50_8xb2-12e_visdrone.py  work_dirs/dino-4scale_r50_8xb2-12e_visdrone/epoch_12.pth --out output/dino/dino.pkl

