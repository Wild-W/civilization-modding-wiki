---
tags:
- EffectType
title: EFFECT_DIPLOMACY_THIRD_PARTY_WARMONGER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_THIRD_PARTY_WARMONGER
>
> * Class: `PLAYERS`
> * Parameters:
>	* LowerLimit `Integer`
>	* PercentOfGrievancesDelta `Integer`

## Samples
```SQL {title="STANDARD_DIPLOMATIC_THIRD_PARTY_WARMONGER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_THIRD_PARTY_WARMONGER",
		"MODIFIER_PLAYER_DIPLOMACY_THIRD_PARTY_WARMONGER",
		"ON_TURN_STARTED",
		"PLAYER_IS_NEW_WARMONGER_SUBJECT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STANDARD_DIPLOMATIC_THIRD_PARTY_WARMONGER",
		"LowerLimit",
		"-40"
	),
	(
		"STANDARD_DIPLOMATIC_THIRD_PARTY_WARMONGER",
		"PercentOfGrievancesDelta",
		10
	);
	
```

