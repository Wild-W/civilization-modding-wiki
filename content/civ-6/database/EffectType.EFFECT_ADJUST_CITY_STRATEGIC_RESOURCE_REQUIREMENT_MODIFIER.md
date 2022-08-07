---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_STRATEGIC_RESOURCE_REQUIREMENT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_STRATEGIC_RESOURCE_REQUIREMENT_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>		* Percentage of discount on strategic resources required for unit production.

## Samples

```SQL {title="BLACK_MARKETEER_STRATEGIC_RESOURCE_COST_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BLACK_MARKETEER_STRATEGIC_RESOURCE_COST_DISCOUNT",
		"MODIFIER_CITY_ADJUST_STRATEGIC_RESOURCE_REQUIREMENT_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BLACK_MARKETEER_STRATEGIC_RESOURCE_COST_DISCOUNT",
		"Amount",
		80
	);
	
```

