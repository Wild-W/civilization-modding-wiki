---
tags:
- EffectType
title: EFFECT_DIPLOMACY_FORCE_INCURSION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_FORCE_INCURSION
>
> * Class: `PLAYERS`
> * Parameters:
>	* IncrementValue `Integer`
>	* InitialValue `Integer`
>	* ReductionValue `Integer`

## Samples

```SQL {title="STANDARD_DIPLOMATIC_INCURSION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_INCURSION",
		"MODIFIER_PLAYER_DIPLOMACY_INCURSION",
		"ON_TURN_STARTED",
		"PLAYER_IS_KNOWN_BUT_NO_OPEN_BORDERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_INCURSION",
		"IncrementValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_INCURSION",
		"InitialValue",
		0
	),
	(
		"STANDARD_DIPLOMATIC_INCURSION",
		"ReductionValue",
		1
	);
	
```

