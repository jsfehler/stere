from typing import Optional

from splinter.element_list import ElementList

from ..decorators import stere_performer
from ..field import Field


@stere_performer('null_action', consumes_arg=False)
class ShadowRoot(Field):
    """Field that uses the shadow-root of an element.

    Only useful as the root of an Area.

    Example:
        >>> address_form = Area(
        >>>     root=ShadowRoot('css', '#addressFormBlock'),
        >>>     address=Input('css', '#userAddress'),
        >>> )

    """

    def find_all(self, wait_time: Optional[int] = None) -> ElementList:
        """Get the shadowRoot element for any found elements.

        Returns:
            ElementList
        """
        found_elements = self._element.find(wait_time)

        shadow_roots = []
        for elem in found_elements:
            shadow_roots.append(elem.shadow_root)

        return ElementList(
            shadow_roots, find_by=self.strategy, query=self.locator,
        )
