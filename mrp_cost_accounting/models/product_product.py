# Copyright 2022 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models, api, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def _set_standard_price(self, value):
        """
        This method is used to filter products that already have the same
        standard price since we are writing that field in every quant
        creation.
        :param value:
        :return:
        """
        self = self.filtered(lambda x: x.standard_price != value)
        return super(ProductProduct, self)._set_standard_price(value)

    # Todo: get price from purchase order
    # def _compute_bom_price(self, bom, boms_to_recompute=False):
    #     self.ensure_one()
    #     if not bom:
    #         return 0
    #     if not boms_to_recompute:
    #         boms_to_recompute = []
    #     total = 0
    #     for opt in bom.routing_id.operation_ids:
    #         duration_expected = (
    #             opt.workcenter_id.time_start +
    #             opt.workcenter_id.time_stop +
    #             opt.time_cycle)
    #         total += (duration_expected / 60) * opt.workcenter_id.costs_hour
    #     for line in bom.bom_line_ids:
    #         if line._skip_bom_line(self):
    #             continue
    #
    #         # Compute recursive if line has `child_line_ids`
    #         if line.child_bom_id and line.child_bom_id in boms_to_recompute:
    #             child_total = line.product_id._compute_bom_price(line.child_bom_id, boms_to_recompute=boms_to_recompute)
    #             total += line.product_id.uom_id._compute_price(child_total, line.product_uom_id) * line.product_qty
    #         else:
    #             total += line.product_id.uom_id._compute_price(line.product_id.standard_price, line.product_uom_id) * line.product_qty
    #     return bom.product_uom_id._compute_price(total / bom.product_qty, self.uom_id)
