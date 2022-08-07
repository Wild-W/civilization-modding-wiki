---
tags:
- EffectType
title: EFFECT_GOVERNOR_ADJUST_IDENITITY_PER_TITLE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GOVERNOR_ADJUST_IDENITITY_PER_TITLE
>
> * Class: `GOVERNORS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="COMMUNICATIONS_OFFICE_GOVERNOR_IDENTITY_PER_TITLE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"COMMUNICATIONS_OFFICE_GOVERNOR_IDENTITY_PER_TITLE",
		"MODIFIER_PLAYER_GOVERNORS_ADJUST_IDENTITY_PER_TITLE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMUNICATIONS_OFFICE_GOVERNOR_IDENTITY_PER_TITLE",
		"Amount",
		1
	);
	
```

