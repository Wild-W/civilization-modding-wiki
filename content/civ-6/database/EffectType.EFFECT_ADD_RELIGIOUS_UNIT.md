---
tags:
- EffectType
title: EFFECT_ADD_RELIGIOUS_UNIT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_RELIGIOUS_UNIT
>
> * Class: `PLAYERS`
> * Parameters:
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="ALLOW_WARRIOR_MONKS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLOW_WARRIOR_MONKS",
		"MODIFIER_PLAYER_RELIGION_ADD_RELIGIOUS_UNIT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLOW_WARRIOR_MONKS",
		"UnitType",
		"UNIT_WARRIOR_MONK"
	);
	
```

