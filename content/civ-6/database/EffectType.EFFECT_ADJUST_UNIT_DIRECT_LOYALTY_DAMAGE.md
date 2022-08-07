---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_DIRECT_LOYALTY_DAMAGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_DIRECT_LOYALTY_DAMAGE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="SPREAD_DISSENT_LOYALTY_DAMAGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPREAD_DISSENT_LOYALTY_DAMAGE",
		"MODIFIER_UNIT_ADJUST_DIRECT_LOYALTY_DAMAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPREAD_DISSENT_LOYALTY_DAMAGE",
		"Amount",
		10
	);
	
```

