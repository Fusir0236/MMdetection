_base_ = 'tood_r50_fpn_1x_coco.py'

# num_classes修改为自己类别
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
    batch_size=8,
    num_workers=4,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/train.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    batch_size=8,
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


default_hooks = dict(logger=dict(type='LoggerHook', interval=1))

# 使用预训练的 Mask R-CNN 模型权重来做初始化，可以提高模型性能
load_from = 'pth_dir/tood_r50_fpn_1x_coco_20211210_103425-20e20746.pth'

# python tools/train.py configs/tood/tood_r50_fpn_1x_myself.py

# python tools/test.py configs/tood/tood_r50_fpn_1x_myself.py work_dirs/tood_r50_fpn_1x_myself/epoch_12.pth --show --show-dir test_save
# python tools/test.py configs/tood/tood_r50_fpn_1x_myself.py work_dirs/tood_r50_fpn_1x_myself/epoch_12.pth --tta

# python tools/test.py configs/tood/tood_r50_fpn_1x_myself.py  work_dirs/tood_r50_fpn_1x_myself/epoch_12.pth --out output/tood/tood.pkl
