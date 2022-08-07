---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ADVANCED_PILLAGING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ADVANCED_PILLAGING
>
> * Class: `UNITS`
> * Parameters:
>	* UseAdvancedPillaging `Boolean`

## Samples

```SQL {title="UNIT_REDUCED_PILLAGE_COST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNIT_REDUCED_PILLAGE_COST",
		"MODIFIER_PLAYER_UNIT_ADJUST_ADVANCED_PILLAGING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_REDUCED_PILLAGE_COST",
		"UseAdvancedPillaging",
		1
	);
	
```

