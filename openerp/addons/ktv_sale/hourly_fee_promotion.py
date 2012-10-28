# -*- coding: utf-8 -*-
#买钟优惠设置
from osv import fields,osv
import ktv_helper

class hourly_fee_promotion(osv.osv):
    '''买钟优惠设置'''
    _name = "ktv.hourly_fee_promotion"
    _description = "买钟优惠设置"

    _columns = {
            "name" : fields.char("name",size = 64,required = True),
            "description" : fields.text("description",size = 255),
            "active" : fields.boolean("active"),
            "is_member" : fields.boolean("is_member",help = "是否会员专属优惠"),
            "buy_minutes" : fields.integer("buy_minutes",help = "买钟时长(分钟)"),
            "present_minutes" :fields.integer("buy_minutes",help = "赠送时长(分钟)"),
            "active_datetime_limit" : fields.boolean("active_datetime_limit",help = "是否启用日期区间限制"),
            "datetime_from" : fields.datetime("datetime_from",help = "起始日期"),
            "datetime_to" : fields.datetime('datetime_to',help = "结束日期"),
            "active_time_limit" : fields.boolean("active_time_limit",help = "是否启用时间段限制"),
            "time_from" : fields.selection(ktv_helper.time_for_selection,"time_from",help = "起始时间"),
            "time_to" : fields.selection(ktv_helper.time_for_selection,"time_to",help = "结束时间"),
            "mon_active": fields.boolean("mon_active"),
            "tue_active": fields.boolean("tue_active"),
            "wed_active": fields.boolean("wed_active"),
            "thurs_active": fields.boolean("thurs_active"),
            "fri_active": fields.boolean("fri_active"),
            "sat_active": fields.boolean("sat_active"),
            "sun_active": fields.boolean("sun_active"),
            }

    _defaults = {
            "is_member" : False,
            "active" : True,
            "active_datetime_limit" : False,
            "active_time_limit" : False,
            "mon_active": False,
            "tue_active": False,
            "wed_active": False,
            "thurs_active": False,
            "fri_active": False,
            "sat_active": False,
            "sun_active": False,
            }


