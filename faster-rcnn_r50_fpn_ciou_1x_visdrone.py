_base_ = 'faster-rcnn_r50_fpn_ciou_1x_coco.py'

# 我们还需要更改 head 中的 num_classes 以匹配数据集中的类别数
model = dict(
    roi_head=dict(
        bbox_head=dict(
            type='Shared2FCBBoxHead',
            num_classes=5
        )
    )
)

# 修改数据集相关配置
data_root ='D:/learnling/vscode-code/mmdetection/data/coco/'

metainfo = {
    'classes':
        ('Dactylogyrus', 'Trichodina', 'hs-Ich', 'ds-Ich', 'Gyrodactylus',),
    # 'palette': [
    #     (220, 20, 60),
    # ]
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

default_hooks = dict(logger=dict(type='LoggerHook', interval=200))

# load_from = 'pth_dir/faster_rcnn_r50_fpn_giou_1x_coco-0eada910.pth'

# python tools/train.py configs/faster_rcnn/faster-rcnn_r50_fpn_ciou_1x_visdrone.py
# python tools/test.py configs/faster_rcnn/faster-rcnn_r50_fpn_ciou_1x_visdrone.py work_dirs/faster-rcnn_r50_fpn_ciou_1x_visdrone/epoch_12.pth --show --show-dir test_save
# python tools/test.py configs/faster_rcnn/faster-rcnn_r50_fpn_ciou_1x_visdrone.py work_dirs/faster-rcnn_r50_fpn_ciou_1x_visdrone/epoch_12.pth --tta

# python tools/test.py configs/faster_rcnn/faster-rcnn_r50_fpn_ciou_1x_visdrone.py  work_dirs/faster-rcnn_r50_fpn_ciou_1x_visdrone/epoch_12.pth --out output/faster_rcnn/faster_rcnn.pkl