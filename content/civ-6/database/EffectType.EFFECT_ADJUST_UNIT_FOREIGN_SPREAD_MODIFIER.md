---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FOREIGN_SPREAD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FOREIGN_SPREAD_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="APOSTLE_FOREIGN_SPREAD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APOSTLE_FOREIGN_SPREAD",
		"MODIFIER_PLAYER_UNIT_ADJUST_FOREIGN_SPREAD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APOSTLE_FOREIGN_SPREAD",
		"Amount",
		200
	);
	
```

