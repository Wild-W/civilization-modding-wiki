---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_UPGRADE_GOODY_HUT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_UPGRADE_GOODY_HUT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GOODY_MILITARY_GRANT_UPGRADE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_MILITARY_GRANT_UPGRADE",
		"MODIFIER_PLAYER_UNIT_ADJUST_UPGRADE_GOODY_HUT",
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
		"GOODY_MILITARY_GRANT_UPGRADE",
		"Amount",
		1
	);
	
```

