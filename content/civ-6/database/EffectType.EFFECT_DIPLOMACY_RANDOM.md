---
tags:
- EffectType
title: EFFECT_DIPLOMACY_RANDOM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_RANDOM
>
> * Class: `PLAYERS`
> * Parameters:
>	* DifficultyOffset `String`
>	* ReductionTurns `Integer`
>	* ReductionValue `Integer`

## Samples

```SQL {title="STANDARD_DIPLOMACY_RANDOM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMACY_RANDOM",
		"MODIFIER_PLAYER_DIPLOMACY_RANDOM",
		"PLAYER_IS_MAJOR_CIV"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value,
		Extra
	)
VALUES
	(
		"STANDARD_DIPLOMACY_RANDOM",
		"DifficultyOffset",
		"LinearScaleFromDefaultHandicap",
		0,
		"-1"
	),
	(
		"STANDARD_DIPLOMACY_RANDOM",
		"ReductionTurns",
		"ARGTYPE_IDENTITY",
		10,
		NULL
	),
	(
		"STANDARD_DIPLOMACY_RANDOM",
		"ReductionValue",
		"ARGTYPE_IDENTITY",
		1,
		NULL
	);
	
```

