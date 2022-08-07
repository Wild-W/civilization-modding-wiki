---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_PERPETUALLY_ON_GUARD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_PERPETUALLY_ON_GUARD
>
> * Class: `PLAYERS`
> * Parameters:
>	* PenaltyPerOccupiedCity `Integer`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`

## Samples
```SQL {title="AGENDA_PERPETUALLY_ON_GUARD_OCCUPATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_PERPETUALLY_ON_GUARD_OCCUPATION",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_PERPETUALLY_ON_GUARD",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_PERPETUALLY_ON_GUARD_OCCUPATION",
		"PenaltyPerOccupiedCity",
		"-2"
	),
	(
		"AGENDA_PERPETUALLY_ON_GUARD_OCCUPATION",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_ON_GUARD_OCCUPY"
	),
	(
		"AGENDA_PERPETUALLY_ON_GUARD_OCCUPATION",
		"StatementKey",
		"LOC_DIPLO_WARNING_LEADER_JOHN_CURTIN_REASON_ANY"
	);
	
```

