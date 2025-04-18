_base_ = 'rtmdet_tiny_8xb32-300e_coco.py'
# num_classes修改
model = dict(
    bbox_head=dict(
        num_classes=5
    )
)

data_root ='D:/learnling/vscode-code/mmdetection/data/coco/'

metainfo = {
    'classes':
        ('id1', 'id2', 'id3', 'id4', 'id5',),
    # 更换自己的数据类别名，我是5分类
    # palette is a list of color tuples, which is used for visualization.
    'palette':
        [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 228), ]
}
train_dataloader = dict(
    batch_size=4,
    num_workers=4,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/train.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    batch_size=4,
    num_workers=4,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/val.json',
        data_prefix=dict(img='valid/')))
test_dataloader = dict(
    batch_size=4,
    num_workers=4,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/test.json',
        data_prefix=dict(img='test/')))

# 修改评价指标相关配置
val_evaluator = dict(ann_file=data_root + 'annotations/val.json')
test_evaluator = dict(ann_file=data_root + 'annotations/test.json')


# optim_wrapper = dict(type='AmpOptimWrapper')

default_hooks = dict(logger=dict(type='LoggerHook', interval=1))
# load_from = 'pth_dir/rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth'

# nohup python tools/train.py configs/rtmdet/rtmdet_tiny_8xb32-300e_visdrone.py
# python tools/test.py configs/rtmdet/rtmdet_tiny_8xb32-300e_visdrone.py work_dirs/rtmdet_tiny_8xb32-300e_visdrone/epoch_300.pth --show --show-dir test_save
# python tools/test.py configs/rtmdet/rtmdet_tiny_8xb32-300e_visdrone.py work_dirs/rtmdet_tiny_8xb32-300e_visdrone/epoch_300.pth --tta
# python tools/analysis_tools/get_flops.py configs/rtmdet/rtmdet_tiny_8xb32-300e_visdrone.py

# python tools/test.py configs/rtmdet/rtmdet_tiny_8xb32-300e_visdrone.py  work_dirs/rtmdet_tiny_8xb32-300e_visdrone/epoch_300.pth --out output/rtmdet/rtmdet.pkl
