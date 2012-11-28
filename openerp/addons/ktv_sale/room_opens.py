# -*- coding: utf-8 -*-
from osv import osv,fields
import decimal_precision as dp
import ktv_helper

class room_opens(osv.osv):
    '''
    包厢开房对象,包括预定转开房和空置转开房
    '''

    _name = "ktv.room_opens"

    _description = "开房信息"

    _columns = {
            "room_operate_id" : fields.many2one('ktv.room_operate',"room_operate_id",required = True),
            "open_time" : fields.datetime('open_time',required = True,readonly = True,help = "开房时间"),
            "saler_id" : fields.many2one('res.users','saler_id',help = "销售经理"),
            "prepay_fee" : fields.float('prepay_fee',digits=(2,10),help = "预付费"),
            "fee_type_id" : fields.many2one("ktv.fee_type","fee_type_id",required = True,help = "计费方式"),
            "price_class_id" : fields.many2one("ktv.price_class","price_class_id",required = True,help = "价格类型"),
            "member_id"    : fields.many2one("ktv.member","member_id",help="会员信息"),
            "guest_name" : fields.char("guest_name",size = 64,help="客人姓名"),
            "persons_count" : fields.integer("persons_count",help="客人人数"),
            #TODO 会员赠送
            #TODO 开房配送
            }

    _defaults = {
            "persons_count" : 2,
            "open_time" : fields.datetime.now()
            }


