_base_ = 'gfl_r50_fpn_1x_coco.py'

# 我们还需要更改 head 中的 num_classes 以匹配数据集中的类别数
model = dict(
    bbox_head=dict(
        num_classes=5
    )
)

# 修改数据集相关配置
data_root ='D:/learnling/vscode-code/mmdetection/data/coco/'

metainfo = {
    'classes':
        ('Dactylogyrus', 'Trichodina', 'hs-Ich', 'ds-Ich', 'Gyrodactylus',),
    # palette is a list of color tuples, which is used for visualization.
    # 'palette':
    #     [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230), (106, 0, 224), ]
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

default_hooks = dict(logger=dict(type='LoggerHook', interval=50))
load_from = 'pth_dir/gfl_r50_fpn_1x_coco_20200629_121244-25944287.pth'

# nohup python tools/train.py configs/gfl/gfl_r50_fpn_1x_visdrone.py
# python tools/test.py configs/gfl/gfl_r50_fpn_1x_visdrone.py work_dirs/gfl_r50_fpn_1x_visdrone/epoch_12.pth --show --show-dir test_save
# python tools/test.py configs/gfl/gfl_r50_fpn_1x_visdrone.py work_dirs/gfl_r50_fpn_1x_visdrone/epoch_12.pth --tta
# python tools/analysis_tools/get_flops.py configs/gfl/gfl_r50_fpn_1x_visdrone.py

# python tools/test.py configs/gfl/gfl_r50_fpn_1x_visdrone.py  work_dirs/gfl_r50_fpn_1x_visdrone/epoch_12.pth --out output/gfl/gfl.pkl