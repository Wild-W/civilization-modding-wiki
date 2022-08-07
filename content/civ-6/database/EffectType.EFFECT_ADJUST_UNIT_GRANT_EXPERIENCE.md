---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_GRANT_EXPERIENCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_GRANT_EXPERIENCE
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TERRACOTTA_ARMY_LEVEL_UP_UNITS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"TERRACOTTA_ARMY_LEVEL_UP_UNITS",
		"MODIFIER_PLAYER_UNITS_ADJUST_GRANT_EXPERIENCE",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TERRACOTTA_ARMY_LEVEL_UP_UNITS",
		"Amount",
		"-1"
	);
	
```

