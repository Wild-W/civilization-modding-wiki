---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_WITH_EXPERIENCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_WITH_EXPERIENCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Experience `Integer`
>	* UniqueOverride `Boolean`
>		* Whether or not to override with unique units
>	* UnitType `String`
>		* [Units.UnitType]

## Samples
```SQL {title="GREATPERSON_THEMISTOCLES_ACTIVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_THEMISTOCLES_ACTIVE",
		"MODIFIER_PLAYER_UNIT_GRANT_UNIT_WITH_EXPERIENCE",
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
		"GREATPERSON_THEMISTOCLES_ACTIVE",
		"Experience",
		0
	),
	(
		"GREATPERSON_THEMISTOCLES_ACTIVE",
		"UniqueOverride",
		1
	),
	(
		"GREATPERSON_THEMISTOCLES_ACTIVE",
		"UnitType",
		"UNIT_QUADRIREME"
	);
	
```

