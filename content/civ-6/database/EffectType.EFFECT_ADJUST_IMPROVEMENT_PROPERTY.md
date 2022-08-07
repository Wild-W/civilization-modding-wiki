---
tags:
- EffectType
title: EFFECT_ADJUST_IMPROVEMENT_PROPERTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IMPROVEMENT_PROPERTY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* Key `Unknown`

## Samples
```SQL {title="SECRET_SOCIETIES_ATTACH_PLAYER_CASTLES_TELEPORT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SECRET_SOCIETIES_ATTACH_PLAYER_CASTLES_TELEPORT",
		"MODIFIER_ALL_PLAYER_IMPROVEMENTS_ADJUST_PROPERTY",
		"THIS_PLOT_IS_A_VAMPIRE_CASTLE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SECRET_SOCIETIES_ATTACH_PLAYER_CASTLES_TELEPORT",
		"Amount",
		1
	),
	(
		"SECRET_SOCIETIES_ATTACH_PLAYER_CASTLES_TELEPORT",
		"Key",
		"PROPERTY_AIRLIFT"
	);
	
```

