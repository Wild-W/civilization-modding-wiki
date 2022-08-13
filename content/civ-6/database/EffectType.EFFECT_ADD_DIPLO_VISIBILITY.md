---
tags:
- EffectType
title: EFFECT_ADD_DIPLO_VISIBILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_DIPLO_VISIBILITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Source `String`
>		* SOURCE_ALLY
>		  SOURCE_DELEGATE
>		  SOURCE_GREAT_PERSON_JOURNALISM
>		  SOURCE_SPY
>		  SOURCE_TECH
>		  SOURCE_TRADER
>		  SOURCE_TRADING_POST_TRAIT
>		  SOURCE_TRAIT
>	* SourceType `String`
>		* DIPLO_SOURCE_ALL_NAMES
>		  DIPLO_SOURCE_FEMALE_ONLY

## Samples

```SQL {title="GREATPERSON_DIPLO_VISIBILITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_DIPLO_VISIBILITY",
		"MODIFIER_PLAYER_ADD_DIPLO_VISIBILITY",
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
		"GREATPERSON_DIPLO_VISIBILITY",
		"Amount",
		1
	),
	(
		"GREATPERSON_DIPLO_VISIBILITY",
		"Source",
		"SOURCE_GREAT_PERSON_JOURNALISM"
	),
	(
		"GREATPERSON_DIPLO_VISIBILITY",
		"SourceType",
		"DIPLO_SOURCE_ALL_NAMES"
	);
	
```

