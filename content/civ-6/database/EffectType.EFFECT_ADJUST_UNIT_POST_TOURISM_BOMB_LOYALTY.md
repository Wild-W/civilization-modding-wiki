---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_POST_TOURISM_BOMB_LOYALTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_POST_TOURISM_BOMB_LOYALTY
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ROCKBAND_INDIE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_INDIE",
		"MODIFIER_SINGLE_UNIT_ADJUST_POST_TOURISM_BOMB_LOYALTY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_INDIE",
		"Amount",
		"-40"
	);
	
```

