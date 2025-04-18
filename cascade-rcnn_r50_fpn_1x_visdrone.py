_base_ = './cascade-rcnn_r50_fpn_1x_coco.py'

data_root ='D:/learnling/vscode-code/mmdetection/data/coco/'

# 我们还需要更改 head 中的 num_classes 以匹配数据集中的类别数
model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                num_classes=5
            ),
            dict(
                type='Shared2FCBBoxHead',
                num_classes=5
            ),
            dict(
                type='Shared2FCBBoxHead',
                num_classes=5
            ),
        ]
    )
)

metainfo = {
    'classes':
        ('Dactylogyrus', 'Trichodina', 'hs-Ich', 'ds-Ich', 'Gyrodactylus',),
    # palette is a list of color tuples, which is used for visualization.
    # 'palette':
    #     [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 228), ]
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

# load_from = 'pth_dir/cascade_rcnn_r50_caffe_fpn_1x_coco_bbox_mAP-0.404_20200504_174853-b857be87.pth'

# python tools/train.py configs/cascade_rcnn/cascade-rcnn_r50_fpn_1x_visdrone.py
# python tools/test.py configs/cascade_rcnn/cascade-rcnn_r50_fpn_1x_visdrone.py work_dirs/cascade-rcnn_r50_fpn_1x_visdrone/epoch_12.pth --show --show-dir test_save
# python tools/test.py configs/cascade_rcnn/cascade-rcnn_r50_fpn_1x_visdrone.py work_dirs/cascade-rcnn_r50_fpn_1x_visdrone/epoch_12.pth --tta

# 输出pkl
# python tools/test.py configs/cascade_rcnn/cascade-rcnn_r50_fpn_1x_visdrone.py  work_dirs/cascade-rcnn_r50_fpn_1x_visdrone/epoch_12.pth --out output/cascade/cascade.pkl