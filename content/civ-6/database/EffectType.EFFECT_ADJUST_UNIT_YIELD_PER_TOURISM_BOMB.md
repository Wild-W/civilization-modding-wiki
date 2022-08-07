---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_YIELD_PER_TOURISM_BOMB
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_YIELD_PER_TOURISM_BOMB
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`

## Samples

```SQL {title="ROCKBAND_POP"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_POP",
		"MODIFIER_PLAYER_UNIT_ADJUST_TOURISM_BOMB_ADDITIONAL_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_POP",
		"Amount",
		"-75"
	),
	(
		"ROCKBAND_POP",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

